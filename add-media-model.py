#!/usr/bin/env python3
import re

# Read the schema file
with open('/home/z/my-project/prisma/schema.prisma', 'r') as f:
    content = f.read()

# Find the User model
user_match = re.search(r'model User {', content)
if not user_match:
    print("Could not find User model")
    exit(1)

user_end = user_match.end()

# Find the Page model after User
page_match = re.search(r'model Page {', content[user_end:])
if not page_match:
    print("Could not find Page model")
    exit(1)

# Find the line where Page model starts
page_start = page_match.start()

# Create the Media model with all fields
media_model = '''
model Media {
  id          String   @id @default(cuid())
  filename    String
  originalName String
  mimeType    String
  size        Int
  url         String
  alt         String?
  caption     String?
  uploadedById String
  uploadedBy  User     @relation(fields: [uploadedById], references: [id])
  status      String   @default("active") // active, deleted
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
'''

# Insert the Media model before the Page model
new_content = content[:page_start] + '\n' + media_model + content[page_start:]

# Write the modified schema
with open('/home/z/my-project/prisma/schema.prisma', 'w') as f:
    f.write(new_content)

print("Successfully added Media model to Prisma schema!")

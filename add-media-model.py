#!/usr/bin/env python3
import re
import os
import sys

# Determine the schema file path
# Try to find schema.prisma in common locations
possible_paths = [
    'prisma/schema.prisma',
    '../prisma/schema.prisma',
    'schema.prisma',
    'schema-part1.prisma'  # Fallback to the schema part in this repo
]

schema_path = None
for path in possible_paths:
    if os.path.exists(path):
        schema_path = path
        break

if not schema_path:
    print("Error: Could not find schema.prisma file")
    print("Tried the following locations:")
    for path in possible_paths:
        print(f"  - {path}")
    sys.exit(1)

print(f"Using schema file: {schema_path}")

# Read the schema file
with open(schema_path, 'r') as f:
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
with open(schema_path, 'w') as f:
    f.write(new_content)

print("Successfully added Media model to Prisma schema!")

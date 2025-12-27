#!/usr/bin/env python3
import re

# Read the schema file
with open('/home/z/my-project/prisma/schema.prisma', 'r') as f:
    content = f.read()

# Update the Media model - add status field and fix uploadedById field
# Replace the closing brace and add status before it
content = re.sub(
    r'updatedAt   DateTime @updatedAt\s*\}\s*\n',
    r'''updatedAt   DateTime @updatedAt
    status      String   @default("active") // active, deleted
}''',
    content
)

# Fix the uploadedById field (change String to User relation)
content = re.sub(
    r'uploadedById String',
    r'''uploadedBy  User     @relation(fields: [uploadedById], references: [id])''',
    content
)

print("Successfully updated Media model with P2 status field!")

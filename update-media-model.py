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

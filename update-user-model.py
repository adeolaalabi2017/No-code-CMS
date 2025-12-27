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

# Update the User model to add P2 advanced user management fields
# Find the role field and add new P2 fields after it
content = re.sub(
    r'role          String    @default\("user"\) \/\/ admin, editor, user\n',
    r'''role          String    @default("user") // admin, editor, user
  twoFactorEnabled     Boolean   @default(false)
  lastLogin            DateTime?
  lastActive           DateTime?
  preferences           String?  // JSON string for user preferences
  ipAddress            String?
  deviceInfo           String?   // User agent string
  auditLogCount        Int      @default(0)
  failedLoginAttempts  Int      @default(0)
  isVerified           Boolean   @default(false) // Email verified status
''',
    content
)

# Add userProfile relation field
content = re.sub(
    r'(\n  activityLog   ActivityLog\[\])',
    r'''\1
  profile              UserProfile? // P2: User profile''',
    content
)

# Write the modified schema back to the file
with open(schema_path, 'w') as f:
    f.write(content)

print("Successfully added P2 advanced user management fields to User model!")

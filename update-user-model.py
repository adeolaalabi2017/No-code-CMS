#!/usr/bin/env python3
import re

# Read the schema file
with open('/home/z/my-project/prisma/schema.prisma', 'r') as f:
    content = f.read()

# Update the User model to add P2 advanced user management fields
# Find the role field and add new P2 fields after it
content = re.sub(
    r'role          String    @default\("user"\) \/\/ admin, editor, user\n)',
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
    r'''\1  activityLog   ActivityLog[]
  profile              UserProfile? // P2: User profile''',
    content
)

print("Successfully added P2 advanced user management fields to User model!")

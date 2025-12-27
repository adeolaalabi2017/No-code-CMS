#!/bin/bash

# Add P2 Media Model to Prisma Schema

# Find the line with "} // Marketplace Theme Models" and add the Media model after it
sed -i '/} \/\/ Marketplace Theme Models/a\

model Media {
  id          String   @id @default(cuid())
  filename    String
  originalName String
  mimeType    String
  size        Int
  url         String
  alt         String?
  caption     String?
  status      String   @default("active") // active, deleted
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  uploadedById String
  uploadedBy  User     @relation(fields: [uploadedById], references: [id])
}
EOF

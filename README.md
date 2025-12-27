# 🚀 No-Code CMS

A modern, intuitive content management system built with Next.js 15, designed for non-technical users to create and manage beautiful websites without coding.

## ✨ Features

- **🎨 Intuitive Admin Dashboard** - Clean, modern interface for managing all your content
- **📄 Pages Management** - Create, edit, and publish website pages with ease
- **📝 Blog System** - Full-featured blogging with categories, tags, and comments
- **🖼️ Media Library** - Upload and organize images, videos, and documents
- **👥 User Management** - Role-based access control (Admin, Editor, User)
- **🔐 Secure Authentication** - NextAuth.js with secure password handling
- **📊 Analytics Dashboard** - Track your site's performance and metrics
- **📱 Responsive Design** - Mobile-first approach that works on all devices
- **🎯 SEO Optimized** - Built-in meta tags and SEO management
- **⚡ Lightning Fast** - Built on Next.js for optimal performance

## ✨ Technology Stack

### 🎯 Core Framework
- **⚡ Next.js 15** - The React framework for production with App Router
- **📘 TypeScript 5** - Type-safe JavaScript for better developer experience
- **🎨 Tailwind CSS 4** - Utility-first CSS framework for rapid UI development

### 🧩 UI Components & Styling
- **🧩 shadcn/ui** - High-quality, accessible components built on Radix UI
- **🎯 Lucide React** - Beautiful & consistent icon library
- **🌈 Framer Motion** - Production-ready motion library for React
- **🎨 Next Themes** - Perfect dark mode in 2 lines of code

### 🔐 Authentication & Database
- **🔐 NextAuth.js** - Complete open-source authentication solution
- **🗄️ Prisma** - Next-generation TypeScript ORM with SQLite
- **🔒 bcryptjs** - Secure password hashing

### 🎨 Advanced UI Features
- **📊 TanStack Table** - Headless UI for building tables and datagrids
- **🖼️ Sharp** - High performance image processing
- **🔔 Sonner** - Beautiful toast notifications

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ or Bun
- A package manager (bun, npm, or yarn)

### Installation

```bash
# Install dependencies
bun install

# Set up the database
bun run db:push

# Generate Prisma client
bun run db:generate

# Start development server
bun run dev
```

Open [http://localhost:3000](http://localhost:3000) to see your application running.

### Initial Setup

1. **Create an Admin Account**
   - Visit [http://localhost:3000/admin/setup](http://localhost:3000/admin/setup)
   - Fill in your name, email, and password
   - Click "Create Admin Account"

2. **Log In**
   - Go to [http://localhost:3000/admin/login](http://localhost:3000/admin/login)
   - Enter your admin credentials
   - You'll be redirected to the dashboard

3. **Start Creating Content**
   - Navigate to "Pages" to create website pages
   - Navigate to "Posts" to write blog articles
   - Manage your media in the "Media Library"
   - Configure your site in "Settings"

## 📁 Project Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── admin/              # Admin panel pages
│   │   ├── login/          # Admin login page
│   │   ├── setup/          # Initial admin account setup
│   │   ├── pages/          # Pages management
│   │   ├── posts/          # Posts management
│   │   ├── media/          # Media library
│   │   └── settings/       # Site settings
│   ├── api/                # API routes
│   │   ├── admin/          # Admin API endpoints
│   │   └── auth/           # Authentication API
│   └── page.tsx            # Landing page
├── components/             # Reusable React components
│   ├── ui/                # shadcn/ui components
│   └── providers.tsx      # Session provider
├── lib/                   # Utility functions
│   ├── auth.ts            # NextAuth configuration
│   ├── db.ts              # Prisma client
│   ├── utils.ts           # Helper functions
│   └── slug.ts            # Slug generation
├── hooks/                 # Custom React hooks
└── middleware.ts          # Route protection middleware

prisma/
└── schema.prisma          # Database schema
```

## 🔧 Available Scripts

```bash
# Development
bun run dev          # Start development server

# Database
bun run db:push      # Push schema changes to database
bun run db:generate  # Generate Prisma client
bun run db:reset     # Reset database

# Code Quality
bun run lint         # Run ESLint

# Production
bun run build        # Build for production
bun run start        # Start production server
```

## 👥 User Roles

- **Admin** - Full access to all features including user management
- **Editor** - Can create and edit content (pages, posts, media)
- **User** - View-only access to the admin panel

## 📝 Current Features

### ✅ Implemented
- Admin dashboard with KPI cards
- Authentication system with NextAuth.js
- Pages management (CRUD operations)
- User management with role-based access
- Media library interface
- Settings module
- Responsive design with sidebar navigation
- Search and filtering capabilities
- Activity logging
- SEO optimization with meta tags

### 🚧 Coming Soon
- Posts/Blog management
- Categories and tags
- Comments system
- Advanced media upload
- Analytics integration
- Theme system
- Multi-language support
- API for third-party integrations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for your own purposes.

---

Built with ❤️ for the developer community. Powered by [Z.ai](https://chat.z.ai) 🚀

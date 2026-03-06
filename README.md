# 👗 Drobe

(insert screenshot)

## Description

Drobe is a community-driven wardrobe sharing platform built with the 
philosophy that fashion should be circular, not disposable. Drobe encourages 
users to extend the life of their clothing by connecting them with people 
who will love their garments just as much as they did.

Every garment on Drobe has a story. Users can share the history behind their 
clothing, showcase their wardrobe, and build meaningful connections through 
local communities — all wrapped up in a wardrobe-inspired UI.

### How It Works

- **List garments** from your wardrobe with details, images, and the story 
  behind each piece
- **Showcase your Drobe** — your personal wardrobe page displays all your 
  garments in a visual, card-based layout
- **Join communities** based on your location or style preferences to 
  connect with like-minded people
- **Build your profile** with a biography, tagline, and profile picture

### Points System (Foundation)

Every garment is assigned a points value based on its condition — laying 
the groundwork for a future exchange economy:

|
 Condition 
|
 Points 
|
|
-----------
|
--------
|
|
 Poor      
|
 1      
|
|
 Fair      
|
 2      
|
|
 Good      
|
 4      
|
|
 Very Good 
|
 8      
|
|
 Excellent 
|
 11     
|

New users start with **10 points**.

## Getting Started

🔗 **[Launch Drobe](⚠️ ADD YOUR DEPLOYED URL HERE)**

📋 **[Planning Materials](⚠️ ADD YOUR PLANNING MATERIALS URL HERE)**

### Current Features

- User authentication (signup, login, logout)
- Full CRUD on garments (create, read, update, delete)
- Full CRUD on communities (create, read, update, delete)
- Profile creation and editing with image upload
- Image upload for garments and communities via Cloudinary
- Community membership (join/leave)
- Wardrobe-inspired UI with trapezoid headers, wardrobe base with feet, 
  and card-based garment displays
- Responsive design — mobile-first with desktop breakpoints

## Attributions

- **[Django](https://www.djangoproject.com/)** — Python web framework
- **[Cloudinary](https://cloudinary.com/)** — Cloud-based image hosting 
  and management
- **[Google Fonts — Aref Ruqaa](https://fonts.google.com/specimen/Aref+Ruqaa)** 
  — Header/logo font
- ⚠️ ADD ANY OTHER LIBRARIES, ICONS, OR ASSETS YOU USED

## Technologies Used

- **Python**
- **Django** — Web framework (MVT architecture)
- **PostgreSQL** — Database (⚠️ or SQLite if using that)
- **Cloudinary** — Image upload and storage
- **HTML5** — Templating with Django Template Language
- **CSS3** — Custom styling (no CSS frameworks)
  - CSS Custom Properties (variables)
  - Flexbox layouts
  - CSS `clip-path` for decorative wardrobe-themed UI
  - CSS pseudo-elements (`::before` / `::after`) for wardrobe feet 
    and border effects
  - Responsive design with media queries
- **Git / GitHub** — Version control
- ⚠️ **Heroku** (or whatever platform you deployed on)

## Next Steps

### Core Functionality
- [ ] **Transaction System** — Allow users to request, approve, and 
      decline garment exchanges (gift, lend, borrow) with points-based 
      economy
- [ ] **Transaction Dashboard** — Filtered views for incoming/outgoing 
      transactions, pending requests, and transaction history
- [ ] **Points Exchange** — Automated points transfer between users 
      when transactions are approved

### Styles & Discovery
- [ ] **Styles Model** — Create a styles system (e.g. vintage, 
      streetwear, minimalist, formal) that can be linked to user 
      profiles and attached as tags to communities, helping users 
      discover the right communities for them

### Community Features
- [ ] **Community Authentication** — Implement an approval-based 
      join system so community admins can vet and approve new 
      members rather than allowing open access
- [ ] **Community Chat** — In-app messaging between community members

### Garment Features
- [ ] **Favourites** — Allow users to favourite garments in other 
      people's Drobes, creating a wishlist of pieces they love
- [ ] **Garment Stories (One-to-Many)** — Evolve the story field into 
      a one-to-many relationship so that anyone who has borrowed a 
      garment can add their own story about their time with it
- [ ] **Garment Journey Timeline** — A visual timeline showing every 
      person a garment has passed through, tracking its path from 
      owner to owner as a one-to-many relationship
- [ ] **Outfit Photos** — A photos section on the garment page where 
      borrowers can upload pictures of themselves wearing the piece, 
      building a gallery of the garment in action

### UI & Personalisation
- [ ] **Wardrobe Door Animation** — Animated wardrobe doors that open 
      when a user visits their Drobe page, revealing their garments 
      inside
- [ ] **Drobe Personalisation** — Let users customise their wardrobe 
      appearance (wood colour, door style, name plate) to make their 
      Drobe feel like their own
- [ ] **Search and Filtering** — Search garments by name, category, 
      size, and condition across the platform
- [ ] **User Ratings and Reviews** — Rate transactions to build trust 
      within the community
- [ ] **Notification System** — Alert users when their garments are 
      requested or transactions are approved/declined
- [ ] **Profile Badges** — Earn badges for milestones (first garment 
      shared, community creator, etc.)
- [ ] **Map View for Communities** — Browse communities on an 
      interactive map based on location
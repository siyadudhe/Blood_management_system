---
name: Vital Ledger
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#5b403d'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#8f6f6c'
  outline-variant: '#e4beba'
  surface-tint: '#ba1a20'
  primary: '#af101a'
  on-primary: '#ffffff'
  primary-container: '#d32f2f'
  on-primary-container: '#fff2f0'
  inverse-primary: '#ffb3ac'
  secondary: '#005faf'
  on-secondary: '#ffffff'
  secondary-container: '#54a0fe'
  on-secondary-container: '#003567'
  tertiary: '#016619'
  on-tertiary: '#ffffff'
  tertiary-container: '#298030'
  on-tertiary-container: '#daffd1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb3ac'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#930010'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#a5c8ff'
  on-secondary-fixed: '#001c3a'
  on-secondary-fixed-variant: '#004786'
  tertiary-fixed: '#9df898'
  tertiary-fixed-dim: '#82db7e'
  on-tertiary-fixed: '#002204'
  on-tertiary-fixed-variant: '#005312'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  sidebar-width: 260px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

The design system is engineered for high-stakes healthcare environments, specifically blood donation management. It balances the inherent urgency of medical logistics with a calming, professional atmosphere. The design narrative centers on **Precision, Trust, and Vitality**.

The aesthetic follows a **Corporate / Modern** approach with subtle **Minimalist** influences. By prioritizing clarity and high-contrast information density, the UI ensures that laboratory technicians and administrative staff can make critical decisions without cognitive overload. The interface uses generous whitespace to denote cleanliness and "sterile" digital environments, while deep crimson accents highlight the life-saving nature of the data.

## Colors

This design system utilizes a high-visibility palette rooted in medical standards. 

- **Primary (Deep Red):** Used for branding, critical alerts, and primary actions. It represents the "Life Force" and urgency of blood supply.
- **Secondary (Clinical Blue):** Used for informational elements, links, and secondary navigation to provide a professional, calming contrast to the red.
- **Tertiary (Success Green):** Specifically reserved for "Safe Levels," successful donations, and positive inventory status.
- **Neutral (Sterile Gray):** A range of cool grays used for backgrounds and borders to maintain a clean, clinical feel.

The system supports a native **Dark Mode** which swaps the #F5F5F5 background for a deep #121212 charcoal, reducing eye strain for 24/7 laboratory operations while maintaining the accessibility of the primary red.

## Typography

**Inter** is the sole typeface for this design system, chosen for its exceptional legibility in data-heavy contexts.

For data tables and inventory lists, utilize the `data-tabular` role which enables tabular figures (monospace numbers) to ensure columns of blood unit counts and expiration dates align perfectly for quick scanning. 

Headlines use a tighter letter-spacing to appear more authoritative, while labels utilize uppercase styling and increased tracking to differentiate them clearly from body text and data values.

## Layout & Spacing

The layout follows a **Fixed Grid** system for desktop to ensure data density remains manageable on widescreen monitors. 

- **Sidebar:** A persistent 260px sidebar is anchored to the left, housing the primary navigation and status indicators.
- **Main Canvas:** Content sits within a 12-column grid with 24px gutters. 
- **Responsive Behavior:** 
  - **Desktop (1024px+):** Full sidebar visible.
  - **Tablet (768px - 1023px):** Sidebar collapses to icons; margins reduce to 16px.
  - **Mobile (<767px):** Sidebar becomes a bottom-bar or hamburger menu; grid shifts to a single column; spacing reduces to the `sm` (8px) and `md` (16px) units to maximize screen real estate.

## Elevation & Depth

To maintain a sterile and professional appearance, this design system uses **Tonal Layers** supplemented by **Ambient Shadows**.

1.  **Level 0 (Background):** #F5F5F5. The foundation.
2.  **Level 1 (Cards/Sidebar):** #FFFFFF. Used for the primary content containers. These use a very soft shadow: `0px 2px 4px rgba(0,0,0,0.05)`.
3.  **Level 2 (Interactive/Modals):** Elements that require focus. These use a more pronounced shadow: `0px 10px 20px rgba(0,0,0,0.08)`.

Avoid heavy blurs or colorful glows. Depth should be used functionally to separate the navigation from the content and the content from the background.

## Shapes

The design system utilizes **Rounded** geometry (8px base) to soften the clinical nature of the application and make the software feel modern and accessible.

- **Standard Elements:** Buttons, Input Fields, and Checkboxes use 8px (`rounded`).
- **Containers:** Dashboard cards and Modals use 16px (`rounded-lg`) to create a clear structural distinction.
- **Status Badges:** Use the `rounded-xl` or full pill-shape to distinguish them from interactive buttons.

## Components

### Buttons & Inputs
Buttons feature solid fills for primary actions (Deep Red) and ghost/outline styles for secondary actions. Inputs must have persistent labels and clear error states in Deep Red. In dark mode, input backgrounds should be slightly lighter than the surface color to maintain visibility.

### Dashboard Cards
Cards are the primary unit of information. They include:
- A top-aligned `label-md` for the metric title.
- A prominent `headline-lg` for the value.
- A small icon in the top right, tinted with the metric's status color (e.g., Red for "Low Stock," Green for "Stable").

### Data Tables
Tables are high-density. Rows should have a subtle hover state (`#F9F9F9`) and use 1px borders for row separation. Use the `data-tabular` typography for all numeric values.

### Sidebar Navigation
The sidebar uses a dark-tinted version of the neutral palette in light mode (e.g., a very deep blue-gray) or pure black in dark mode to provide a "frame" for the main content. Active states are indicated by a 4px vertical "Primary Red" bar on the left edge of the menu item.

### Chips & Tags
Use chips for blood types (A+, O-, etc.). These should be color-coded only when indicating inventory alerts; otherwise, they remain neutral to avoid visual clutter.
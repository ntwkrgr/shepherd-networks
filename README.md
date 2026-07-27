# Shepherd Networks

Professional network consulting website for Shepherd Networks LLC, serving San Angelo, TX and the Concho Valley.

## About

Shepherd Networks provides expert network consulting services for residential and commercial clients, including:

- **Network Performance & Security Bundle** — Monitoring, DNS security, and remote support
- **Network Monitoring** — 24/7 availability tracking with proactive alerts
- **DNS Security** — Managed secure DNS with custom filtering
- **Equipment Installation & Setup** — Switches, access points, and IP cameras
- **New Construction & Remodel Network Design** — Structured cabling plans and equipment placement
- **Wireless Network Design** — Site surveys, AP placement, and VLAN planning
- **Troubleshooting & Optimization** — Diagnostics, performance tuning, and security audits
- **Security Camera Consulting & Design** — Camera placement, NVR/DVR selection, and remote viewing

## Tech Stack

- [Jekyll](https://jekyllrb.com/) — Static site generator
- HTML / CSS / JavaScript
- [Lucide Icons](https://lucide.dev/)
- [Formspree](https://formspree.io/) — Contact form handling

## Local Development

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) 3.3.11
- [Bundler](https://bundler.io/)

### Setup

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

Commit `Gemfile.lock` whenever dependencies change so local and GitHub Pages
builds use the same dependency set.

## Project Structure

```
├── _config.yml        # Jekyll configuration
├── _includes/         # Reusable HTML partials (header, footer)
├── _layouts/          # Page layout templates
├── assets/
│   ├── css/           # Stylesheets
│   ├── images/        # Logos and graphics
│   └── js/            # JavaScript
├── docs/
│   ├── legal/         # Legal documents (MSA, privacy policy, ToS, NDA)
│   ├── service-agreements/  # Per-service client agreements
│   ├── service-notes/       # Internal service notes and SLA drafts
│   └── templates/     # Invoice, quote, and assessment templates
├── index.html         # Main homepage
├── contact.html       # Contact page
├── services.html      # Services page
├── rates.html         # Pricing page
└── CNAME              # Custom domain configuration
```

## License

All rights reserved © Shepherd Networks LLC.

import json
import html
import os

ASSET_PREFIX = "PIB%20Delhi,%20Press%20Information%20Bureau_files/"

from generate_current_page import (
    slides_data, pm_links, releases_data, explainers_data,
    advisories_data, videos_data, photos_data, blogs_data
)

def build_current_page():
    # Convert data structures to JSON strings for embedded JS
    slides_json = json.dumps(slides_data)
    releases_json = json.dumps(releases_data)
    explainers_json = json.dumps(explainers_data)
    videos_json = json.dumps(videos_data)
    photos_json = json.dumps(photos_data)
    blogs_json = json.dumps(blogs_data)

    parts = []

    # HTML HEAD & STYLES
    parts.append(f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Press Information Bureau — Government of India | पत्र सूचना कार्यालय</title>
  <meta name="description" content="Official website of the Press Information Bureau (PIB), Government of India. The nodal agency for disseminating information on government policies, decisions, and development initiatives.">
  <meta name="keywords" content="PIB, Press Information Bureau, Government of India, Press Releases, PM Modi, Cabinet Decisions, Explainers, Fact Check">
  <meta name="theme-color" content="#162F6A">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{ASSET_PREFIX}pib-logo_-0eu.png">
  <link rel="apple-touch-icon" href="{ASSET_PREFIX}pib-logo_-0eu.png">

  <!-- Fonts & Tailwind -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            pib: {{
              50: '#f0f5ff',
              100: '#e5eeff',
              200: '#cddcff',
              500: '#3b6ecc',
              700: '#162F6A',
              800: '#0F204A',
              900: '#0B1B3D',
              saffron: '#FF671F',
              saffrondark: '#E65100',
              green: '#138808',
              greendark: '#0B5904',
              gold: '#D97706'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            serif: ['"Merriweather"', 'Georgia', 'serif'],
            devanagari: ['"Noto Sans Devanagari"', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
      --color-primary: #162F6A;
      --color-primary-dark: #0B1B3D;
      --color-saffron: #FF671F;
      --color-green: #138808;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
    }}
    .font-serif-title {{
      font-family: 'Merriweather', Georgia, serif;
    }}
    .devanagari-font {{
      font-family: 'Noto Sans Devanagari', sans-serif;
    }}
    /* High contrast mode overrides */
    .high-contrast {{
      filter: contrast(125%);
    }}
    .high-contrast body {{
      background-color: #000000 !important;
      color: #FFFFFF !important;
    }}
    .high-contrast .card, .high-contrast article, .high-contrast nav, .high-contrast header, .high-contrast footer {{
      background-color: #121212 !important;
      color: #FFFFFF !important;
      border-color: #FFFF00 !important;
    }}
    .high-contrast a {{
      color: #FFFF00 !important;
      text-decoration: underline !important;
    }}
    /* Clean focus outlines */
    *:focus-visible {{
      outline: 2px solid #162F6A;
      outline-offset: 2px;
    }}
    .dark *:focus-visible {{
      outline: 2px solid #60A5FA;
      outline-offset: 2px;
    }}
    /* Custom scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F1F5F9;
    }}
    .dark ::-webkit-scrollbar-track {{
      background: #18181B;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 4px;
    }}
    .dark ::-webkit-scrollbar-thumb {{
      background: #3F3F46;
    }}
    /* Subtle animations */
    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
    }}
    .pulse-live {{
      animation: pulseDot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-zinc-950 dark:text-zinc-100 flex flex-col min-h-screen transition-colors duration-200">

  <!-- A11y Skip Link -->
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-pib-700 focus:text-white focus:rounded-md focus:shadow-xl focus:font-semibold">
    Skip to main content | मुख्य सामग्री पर जाएं
  </a>

  <!-- TOP TRICOLOR ACCENT BAR -->
  <div class="h-1.5 w-full grid grid-cols-3" aria-hidden="true">
    <div class="bg-[#FF671F]"></div>
    <div class="bg-white border-y border-slate-200 dark:border-zinc-800"></div>
    <div class="bg-[#138808]"></div>
  </div>

  <!-- LEVEL 1: TOP ACCESSIBILITY & UTILITY BAR -->
  <aside aria-label="Accessibility & Utility Controls" class="bg-pib-900 text-white text-xs py-1.5 px-4 sm:px-6 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-y-2">
      <!-- Left: National Portal & Screen Reader -->
      <div class="flex items-center gap-3">
        <a href="https://www.india.gov.in" target="_blank" rel="noopener noreferrer" class="hover:text-amber-300 transition-colors flex items-center gap-1 font-medium">
          <span>भारत सरकार</span>
          <span class="text-white/40">|</span>
          <span>Government of India</span>
        </a>
        <span class="text-white/30 hidden sm:inline">|</span>
        <a href="#main-content" class="hidden sm:inline hover:text-amber-300 transition-colors">
          Screen Reader Access
        </a>
      </div>

      <!-- Right: Controls & Time -->
      <div class="flex items-center gap-4 flex-wrap">
        <!-- Live Clock -->
        <div id="live-clock" class="text-white/80 font-mono tracking-tight hidden md:inline" aria-label="Current Date and Time">
          Thu, 13 August 2026 | 02:45 PM IST
        </div>

        <div class="h-3.5 w-px bg-white/20 hidden md:inline" aria-hidden="true"></div>

        <!-- Font Resizer -->
        <div class="flex items-center bg-white/10 rounded px-1 py-0.5 border border-white/15" role="group" aria-label="Font size adjustment">
          <button id="btn-font-dec" class="px-1.5 py-0.5 hover:bg-white/20 rounded font-semibold text-xs" title="Decrease font size" aria-label="Decrease text size">A-</button>
          <button id="btn-font-reset" class="px-1.5 py-0.5 hover:bg-white/20 rounded font-semibold text-xs border-x border-white/15" title="Reset font size" aria-label="Reset text size to standard">A</button>
          <button id="btn-font-inc" class="px-1.5 py-0.5 hover:bg-white/20 rounded font-semibold text-xs" title="Increase font size" aria-label="Increase text size">A+</button>
        </div>

        <!-- Contrast Toggle -->
        <button id="btn-contrast" class="hover:text-amber-300 transition-colors flex items-center gap-1" title="High Contrast Mode" aria-label="Toggle high contrast mode">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
          <span class="hidden sm:inline">Contrast</span>
        </button>

        <!-- Dark Mode Toggle -->
        <button id="btn-theme-toggle" class="hover:text-amber-300 transition-colors flex items-center gap-1" title="Dark / Light mode" aria-label="Toggle dark mode">
          <svg id="theme-moon-icon" class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
          <span class="hidden sm:inline">Dark</span>
        </button>

        <!-- Language Selector -->
        <div class="relative">
          <label for="lang-select" class="sr-only">Select Language</label>
          <select id="lang-select" class="bg-white/10 text-white rounded px-2 py-0.5 text-xs border border-white/20 hover:bg-white/20 cursor-pointer focus:outline-none focus:ring-1 focus:ring-amber-400">
            <option value="en" class="bg-zinc-900 text-white" selected>English</option>
            <option value="hi" class="bg-zinc-900 text-white">हिन्दी (Hindi)</option>
            <option value="ur" class="bg-zinc-900 text-white">اردو (Urdu)</option>
            <option value="ta" class="bg-zinc-900 text-white">தமிழ் (Tamil)</option>
            <option value="te" class="bg-zinc-900 text-white">తెలుగు (Telugu)</option>
            <option value="bn" class="bg-zinc-900 text-white">বাংলা (Bengali)</option>
            <option value="mr" class="bg-zinc-900 text-white">मराठी (Marathi)</option>
            <option value="gu" class="bg-zinc-900 text-white">ગુજરાતી (Gujarati)</option>
          </select>
        </div>
      </div>
    </div>
  </aside>

  <!-- LEVEL 2: MAIN BRAND IDENTITY HEADER -->
  <header class="bg-white dark:bg-zinc-900 border-b border-slate-200 dark:border-zinc-800 transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 sm:py-4 flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Emblem & Title Brandmark -->
      <div class="flex items-center gap-3 sm:gap-4">
        <a href="#" class="shrink-0 group focus:outline-none" aria-label="Go to PIB Homepage">
          <img src="{ASSET_PREFIX}emblem-of-india_-0eu.png" alt="State Emblem of India" class="h-12 sm:h-14 w-auto object-contain dark:invert transition-transform group-hover:scale-105">
        </a>
        <div class="flex flex-col">
          <span class="text-xs sm:text-sm font-semibold tracking-wide text-slate-600 dark:text-zinc-400">
            भारत सरकार <span class="font-normal text-slate-400 dark:text-zinc-500">|</span> Government of India
          </span>
          <h1 class="text-lg sm:text-2xl font-bold tracking-tight text-pib-700 dark:text-blue-400 leading-tight">
            पत्र सूचना कार्यालय
          </h1>
          <span class="text-xs sm:text-sm font-semibold tracking-wide text-slate-700 dark:text-zinc-300">
            Press Information Bureau
          </span>
        </div>
      </div>

      <!-- Center / Right: PIB Logo & Quick Search -->
      <div class="flex items-center gap-4 sm:gap-6 w-full md:w-auto justify-between md:justify-end">
        <!-- Live Quick Search -->
        <div class="relative flex-1 md:w-72 lg:w-80">
          <label for="global-search" class="sr-only">Search press releases, explainers, and archives</label>
          <div class="relative flex items-center">
            <input type="search" id="global-search" placeholder="Search PIB releases, ministries..." 
                   class="w-full bg-slate-100 dark:bg-zinc-800 text-slate-800 dark:text-zinc-100 text-xs sm:text-sm rounded-full pl-9 pr-4 py-2 border border-slate-200 dark:border-zinc-700 focus:outline-none focus:ring-2 focus:ring-pib-700 dark:focus:ring-blue-400 transition-all shadow-inner">
            <svg class="w-4 h-4 text-slate-400 dark:text-zinc-400 absolute left-3 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>

        <!-- Official PIB Logo Brandmark -->
        <a href="#" class="shrink-0 group focus:outline-none" aria-label="PIB Logo">
          <img src="{ASSET_PREFIX}pib-logo_-0eu.png" alt="PIB Logo" class="h-10 sm:h-12 w-auto object-contain transition-transform group-hover:scale-105">
        </a>
      </div>

    </div>
  </header>

  <!-- LEVEL 3: STICKY NAVIGATION BAR WITH READING PROGRESS -->
  <nav id="sticky-navbar" aria-label="Main Navigation" class="sticky top-0 z-40 bg-pib-700 dark:bg-zinc-900 text-white shadow-md transition-all duration-300 border-b border-pib-800 dark:border-zinc-800">
    <!-- Reading Progress Bar -->
    <div id="scroll-progress-bar" class="h-1 bg-amber-400 w-0 transition-all duration-75" aria-hidden="true"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="flex items-center justify-between h-12">
        
        <!-- Navigation Links -->
        <div class="flex items-center gap-1 sm:gap-2 overflow-x-auto scrollbar-none py-1">
          <a href="#frontpage" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap active-nav-link text-amber-300">
            Front Page
          </a>
          <a href="#releases" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Press Releases
          </a>
          <a href="#explainers" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Explainers
          </a>
          <a href="#media-desk" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap flex items-center gap-1.5">
            <span>Media Desk</span>
            <span class="inline-block w-2 h-2 rounded-full bg-amber-400 pulse-live" title="Live advisories available"></span>
          </a>
          <a href="#fact-check" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap text-amber-200 hover:text-amber-300">
            Fact Check Unit
          </a>
          <a href="#videos" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Videos
          </a>
          <a href="#photos" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Photos
          </a>
          <a href="#blogs" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Blogs &amp; Features
          </a>
          <a href="#directory" class="px-3 py-1.5 rounded text-xs sm:text-sm font-semibold hover:bg-white/10 transition-colors whitespace-nowrap">
            Regional &amp; RTI
          </a>
        </div>

        <!-- Right Side: Archives / External Portals Quick Pill -->
        <div class="hidden lg:flex items-center gap-2 pl-3 border-l border-white/20 text-xs">
          <a href="/del/en/archives" class="px-2.5 py-1 rounded bg-white/10 hover:bg-white/20 transition-colors font-medium">
            Archives
          </a>
          <a href="https://pib.gov.in" target="_blank" rel="noopener noreferrer" class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-600 text-pib-900 font-bold transition-colors">
            National Portal ↗
          </a>
        </div>

      </div>
    </div>
  </nav>

  <!-- LIVE BREAKING NEWS / FLASH ANNOUNCEMENTS TICKER -->
  <div class="bg-amber-50 dark:bg-amber-950/40 border-b border-amber-200 dark:border-amber-900/50 text-xs py-2 px-4 sm:px-6">
    <div class="max-w-7xl mx-auto flex items-center gap-3">
      <div class="shrink-0 flex items-center gap-1.5 bg-pib-saffrondark text-white font-bold px-2 py-0.5 rounded text-[11px] uppercase tracking-wider">
        <span class="w-2 h-2 rounded-full bg-white pulse-live"></span>
        <span>Latest Update</span>
      </div>
      <div class="flex-1 overflow-hidden relative">
        <p id="ticker-text" class="truncate font-medium text-slate-800 dark:text-zinc-200">
          <a href="/del/en/press-releases/national-biodiversity-authority-releases-rs-15-52-crore-abs-proceeds-from-mustar-2298712" class="hover:underline">
            National Biodiversity Authority releases Rs. 15.52 crore ABS Proceeds from Mustard Genetic Resources
          </a>
          <span class="mx-3 text-slate-400">|</span>
          <a href="/del/en/press-releases/prime-minister-shares-a-sanskrit-subhashitam-highlighting-determination-persever-2298710" class="hover:underline">
            PM shares Sanskrit Subhashitam on determination and perseverance
          </a>
          <span class="mx-3 text-slate-400">|</span>
          <a href="/del/en/press-releases/press-release-on-393rd-report-of-the-department-related-parliamentary-standing-c-2298703" class="hover:underline">
            393rd Report of Parliamentary Standing Committee on Transport, Tourism &amp; Culture tabled
          </a>
        </p>
      </div>
      <button id="ticker-pause-btn" class="shrink-0 text-slate-500 hover:text-slate-800 dark:text-zinc-400 dark:hover:text-zinc-100" title="Pause / Play Ticker" aria-label="Pause ticker updates">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      </button>
    </div>
  </div>

  <!-- MAIN CONTENT CONTAINER -->
  <main id="main-content" class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-12">

    <!-- ========================================== -->
    <!-- SECTION 1: FRONT PAGE HERO & PM CORNER    -->
    <!-- ========================================== -->
    <section id="frontpage" aria-label="Front Page and Prime Minister's Corner" class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
      
      <!-- LEFT 8 COLS: 10-SLIDE HERO BANNER CAROUSEL -->
      <div class="lg:col-span-8 flex flex-col">
        <div class="relative bg-black rounded-2xl overflow-hidden shadow-lg border border-slate-200 dark:border-zinc-800 group h-[360px] sm:h-[440px] md:h-[480px]">
          
          <!-- Slide Images Container -->
          <div id="carousel-slides-container" class="relative w-full h-full" aria-live="polite">
""")

    for i, slide in enumerate(slides_data):
        active_class = "opacity-100 z-10" if i == 0 else "opacity-0 z-0 pointer-events-none"
        parts.append(f"""
            <div class="carousel-slide absolute inset-0 transition-opacity duration-700 ease-in-out {active_class}" data-slide-index="{i}">
              <img src="{slide['img']}" alt="{html.escape(slide['caption'])}" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent"></div>
              
              <!-- Frosted Glass Caption Card -->
              <div class="absolute bottom-4 left-4 right-4 sm:bottom-6 sm:left-6 sm:right-6 bg-slate-900/80 backdrop-blur-md rounded-xl p-4 sm:p-5 border border-white/20 text-white shadow-xl">
                <div class="flex items-center justify-between gap-2 mb-2">
                  <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500 text-slate-900 uppercase tracking-wider">
                    {slide['category']}
                  </span>
                  <span class="text-xs text-white/70 font-mono">
                    {slide['date']}
                  </span>
                </div>
                <p class="text-sm sm:text-base md:text-lg font-medium leading-snug line-clamp-2">
                  {slide['caption']}
                </p>
              </div>
            </div>
        """)

    parts.append("""
          </div>

          <!-- Carousel Controls: Prev / Next Arrows -->
          <button id="btn-carousel-prev" class="absolute left-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 rounded-full bg-black/60 hover:bg-black/80 text-white border border-white/30 flex items-center justify-center transition-all opacity-80 hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-amber-400" aria-label="Previous slide">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
          </button>
          <button id="btn-carousel-next" class="absolute right-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 rounded-full bg-black/60 hover:bg-black/80 text-white border border-white/30 flex items-center justify-center transition-all opacity-80 hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-amber-400" aria-label="Next slide">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
          </button>

          <!-- Top Status: Slide Counter & Pause/Play -->
          <div class="absolute top-4 right-4 z-20 flex items-center gap-2 bg-black/60 backdrop-blur-sm rounded-full px-3 py-1 text-xs text-white border border-white/20">
            <span id="carousel-counter" class="font-mono">1 / 10</span>
            <span class="text-white/40">|</span>
            <button id="btn-carousel-pause" class="hover:text-amber-400 transition-colors" title="Pause automatic rotation" aria-label="Pause slide rotation">
              <svg id="carousel-play-icon" class="w-3.5 h-3.5 hidden" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg id="carousel-pause-icon" class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
          </div>

        </div>

        <!-- Carousel Pagination Dots -->
        <div id="carousel-dots-container" class="flex items-center justify-center gap-2 mt-3" role="tablist" aria-label="Slide indicators">
    """)

    for i in range(len(slides_data)):
        active_pill = "bg-pib-700 dark:bg-amber-400 w-8" if i == 0 else "bg-slate-300 dark:bg-zinc-700 w-2.5"
        parts.append(f"""
          <button class="carousel-dot h-2.5 rounded-full transition-all duration-300 {active_pill}" data-dot-index="{i}" role="tab" aria-selected="{'true' if i==0 else 'false'}" aria-label="Go to slide {i+1}"></button>
        """)

    parts.append(f"""
        </div>
      </div>

      <!-- RIGHT 4 COLS: PRIME MINISTER CORNER -->
      <div class="lg:col-span-4 flex flex-col">
        <div class="bg-gradient-to-b from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-900/90 rounded-2xl p-5 sm:p-6 shadow-md border border-slate-200 dark:border-zinc-800 flex flex-col justify-between h-full relative overflow-hidden">
          
          <div class="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-amber-400 via-pib-saffron to-amber-500"></div>

          <div>
            <!-- Section Title -->
            <div class="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-zinc-800">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                <h2 class="text-xs font-bold tracking-wider uppercase text-pib-700 dark:text-amber-400">
                  Prime Minister's Desk
                </h2>
              </div>
              <span class="text-[11px] text-slate-500 dark:text-zinc-400 font-medium">PMO Updates</span>
            </div>

            <!-- Leader Portrait & Title -->
            <div class="flex items-center gap-4 mb-5">
              <div class="relative shrink-0 w-20 h-20 rounded-full overflow-hidden ring-4 ring-amber-400/30 bg-amber-50 dark:bg-zinc-800 shadow-md">
                <img src="{ASSET_PREFIX}prime-minister_-0eu.png" alt="Shri Narendra Modi, Hon'ble Prime Minister of India" class="w-full h-full object-cover">
              </div>
              <div>
                <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-tight">
                  Shri Narendra Modi
                </h3>
                <p class="text-xs text-slate-600 dark:text-zinc-400 font-medium mt-0.5">
                  Hon'ble Prime Minister of India
                </p>
                <div class="flex items-center gap-2 mt-2">
                  <a href="https://www.pmindia.gov.in" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-[11px] font-semibold text-pib-700 dark:text-amber-400 hover:underline">
                    <span>pmindia.gov.in</span>
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                  </a>
                </div>
              </div>
            </div>

            <!-- Action Badges Grid (All 8 authentic links) -->
            <div class="grid grid-cols-2 gap-2 text-xs">
    """)

    for link in pm_links:
        ext_icon = ' <span class="text-[10px] opacity-70">↗</span>' if link.get("ext") else ""
        target = ' target="_blank" rel="noopener noreferrer"' if link.get("ext") else ""
        parts.append(f"""
              <a href="{link['url']}"{target} class="p-2.5 rounded-xl bg-white dark:bg-zinc-800/80 hover:bg-pib-50 dark:hover:bg-zinc-800 border border-slate-200 dark:border-zinc-700/80 hover:border-pib-700 dark:hover:border-amber-400/50 transition-all group flex flex-col justify-center shadow-xs">
                <span class="font-bold text-slate-800 dark:text-zinc-200 group-hover:text-pib-700 dark:group-hover:text-amber-400 transition-colors">
                  {link['title']}{ext_icon}
                </span>
                <span class="text-[10px] text-slate-500 dark:text-zinc-400 line-clamp-1 mt-0.5">
                  {link['desc']}
                </span>
              </a>
        """)

    parts.append("""
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-zinc-800 text-[11px] text-slate-500 dark:text-zinc-400 flex items-center justify-between">
            <span>Direct citizen interaction portal</span>
            <a href="https://www.pmindia.gov.in" target="_blank" rel="noopener noreferrer" class="font-bold text-pib-700 dark:text-amber-400 hover:underline">Connect ↗</a>
          </div>

        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: PRESS RELEASES (LEAD & RIVER)  -->
    <!-- ========================================== -->
    <section id="releases" aria-label="Press Releases" class="scroll-mt-24 space-y-5">
      
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-3 border-b-2 border-pib-700 dark:border-blue-500">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-pib-saffrondark uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-pib-saffrondark rounded-full"></span>
            <span>Official Dispatches</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Press Releases</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| प्रेस विज्ञप्तियां</span>
          </h2>
        </div>

        <!-- Right Controls: View Switcher & Tabs -->
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <!-- View Switcher: Split vs Grid -->
          <div class="flex items-center bg-slate-200/80 dark:bg-zinc-800 p-0.5 rounded-xl border border-slate-300 dark:border-zinc-700" role="group" aria-label="Layout view switcher">
            <button id="btn-view-split" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-white dark:bg-zinc-700 text-pib-700 dark:text-white shadow-xs flex items-center gap-1.5 transition-all" title="Lead & River Editorial View" aria-pressed="true">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2"></path></svg>
              <span>Lead &amp; River</span>
            </button>
            <button id="btn-view-grid" class="px-3 py-1.5 rounded-lg text-xs font-bold text-slate-600 dark:text-zinc-400 hover:text-pib-700 dark:hover:text-white flex items-center gap-1.5 transition-all" title="Full Grid View" aria-pressed="false">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
              <span>Grid</span>
            </button>
          </div>

          <!-- Category Filter Tabs: Latest, Top, Most Read -->
          <div class="flex items-center gap-1 bg-slate-200/80 dark:bg-zinc-800 p-1 rounded-xl" role="tablist" aria-label="Press Release Categories">
            <button id="tab-rel-latest" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white dark:bg-zinc-700 text-pib-700 dark:text-white shadow-xs" role="tab" aria-selected="true">
              Latest
            </button>
            <button id="tab-rel-top" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-pib-700 dark:hover:text-white" role="tab" aria-selected="false">
              Top
            </button>
            <button id="tab-rel-mostread" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-pib-700 dark:hover:text-white" role="tab" aria-selected="false">
              Most Read
            </button>
          </div>
        </div>
      </div>

      <!-- Real-time Filter & Keyword Search Bar + Quick Ministry Chips -->
      <div class="bg-white dark:bg-zinc-900 p-3.5 rounded-2xl border border-slate-200 dark:border-zinc-800 shadow-xs space-y-3">
        <div class="flex flex-col sm:flex-row items-center gap-3">
          <div class="relative flex-1 w-full">
            <input type="text" id="releases-keyword-filter" placeholder="Filter dispatches by keyword, ministry, or topic..." 
                   class="w-full bg-slate-50 dark:bg-zinc-800 text-slate-800 dark:text-zinc-100 text-xs sm:text-sm rounded-xl pl-9 pr-3 py-2 border border-slate-200 dark:border-zinc-700 focus:outline-none focus:ring-2 focus:ring-pib-700 dark:focus:ring-blue-400">
            <svg class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <div class="flex items-center gap-3 w-full sm:w-auto justify-between shrink-0">
            <span id="releases-count-badge" class="text-xs font-semibold text-slate-500 dark:text-zinc-400 whitespace-nowrap">
              Showing releases 1–6 of 15
            </span>
            <a href="/del/en/press-releases" class="text-xs font-bold text-pib-700 dark:text-blue-400 hover:underline whitespace-nowrap">
              Archive Directory ↗
            </a>
          </div>
        </div>

        <!-- Quick Ministry Filter Chips -->
        <div class="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-0.5" id="ministry-filter-chips" role="group" aria-label="Filter by Ministry">
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-pib-700 text-white transition-all whitespace-nowrap" data-ministry="">All Ministries</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Prime Minister">PMO</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Environment">Environment</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Commerce">Commerce &amp; Industry</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Home Affairs">Home Affairs</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Electronics">Electronics &amp; IT</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Health">Health &amp; Family Welfare</button>
          <button class="chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap" data-ministry="Corporate Affairs">Corporate Affairs</button>
        </div>
      </div>

      <!-- VIEW 1: STYLISH EDITORIAL SPLIT (LEAD ON LEFT + RIVER ON RIGHT) -->
      <div id="releases-split-view" class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        <!-- LEFT: Featured Lead Story Card (5 cols) -->
        <div class="lg:col-span-5 bg-white dark:bg-zinc-900 rounded-2xl border border-slate-200 dark:border-zinc-800 shadow-sm p-4 sm:p-5 flex flex-col justify-between relative overflow-hidden transition-all duration-300" id="lead-story-card">
          <!-- Subtle top saffron accent bar -->
          <div class="absolute top-0 inset-x-0 h-1.5 bg-gradient-to-r from-pib-700 via-amber-500 to-pib-saffron"></div>

          <div>
            <!-- Top Visual Frame (Image/Thumbnail) -->
            <a id="lead-story-img-link" href="/del/en/press-releases/national-biodiversity-authority-releases-rs-15-52-crore-abs-proceeds-from-mustar-2298712" class="relative w-full h-32 sm:h-36 rounded-xl overflow-hidden mb-3 bg-slate-50 dark:bg-zinc-800/80 border border-slate-200/60 dark:border-zinc-700/60 flex items-center justify-center shrink-0 group block cursor-pointer">
              <img id="lead-story-img" src="PIB%20Delhi,%20Press%20Information%20Bureau_files/moef_gov_in_-0eu.avif" alt="National Biodiversity Authority" class="w-16 h-16 sm:w-20 sm:h-20 object-contain p-1.5 group-hover:scale-105 transition-all duration-300">
              <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent pointer-events-none"></div>
            </a>

            <!-- Eyebrow: Lead Badge + Read time -->
            <div class="flex items-center justify-between gap-2 mb-2">
              <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-bold bg-pib-700 text-white uppercase tracking-wider">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400 pulse-live"></span>
                <span>Lead Story / मुख्य समाचार</span>
              </span>
              <span id="lead-story-readtime" class="text-[11px] text-slate-500 dark:text-zinc-400 font-mono">
                9 min read
              </span>
            </div>

            <!-- Ministry Tag -->
            <div class="mb-1.5">
              <span id="lead-story-ministry" class="text-xs font-bold text-pib-saffrondark dark:text-amber-400">
                Ministry of Environment, Forest and Climate Change
              </span>
            </div>

            <!-- Title -->
            <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-snug line-clamp-2 hover:text-pib-700 dark:hover:text-blue-400 transition-colors">
              <a id="lead-story-title-link" href="/del/en/press-releases/national-biodiversity-authority-releases-rs-15-52-crore-abs-proceeds-from-mustar-2298712">
                National Biodiversity Authority releases Rs. 15.52 crore ABS Proceeds from Mustard Genetic Resources
              </a>
            </h3>

            <!-- Bullets / Takeaways Container -->
            <div class="mt-3 pt-2.5 border-t border-slate-100 dark:border-zinc-800">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1.5">Key Highlights:</span>
              <ul id="lead-story-bullets" class="space-y-1.5 text-xs text-slate-700 dark:text-zinc-300 leading-relaxed">
                <li class="flex items-start gap-2">
                  <span class="text-pib-700 dark:text-blue-400 font-bold shrink-0 mt-0.5">●</span>
                  <span class="line-clamp-2">The National Biodiversity Authority (NBA) has released Rs. 15.52 crore in Access and Benefit Sharing (ABS) proceeds.</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-pib-700 dark:text-blue-400 font-bold shrink-0 mt-0.5">●</span>
                  <span class="line-clamp-2">Proceeds received from M/s Pioneer Overseas Corporation, which developed ten commercial mustard hybrid varieties using India's biological resources.</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Bottom Action Row -->
          <div class="mt-3.5 pt-2.5 border-t border-slate-100 dark:border-zinc-800 flex items-center justify-between">
            <div class="flex items-center gap-1.5 text-[11px] text-slate-500 font-mono">
              <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <time id="lead-story-date">13 August 2026</time>
            </div>
            <div class="flex items-center gap-1.5">
              <button id="lead-story-share" class="p-1.5 hover:bg-slate-100 dark:hover:bg-zinc-800 rounded-full transition-colors text-slate-500 hover:text-slate-800" title="Share release">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
              </button>
              <a id="lead-story-cta" href="/del/en/press-releases/national-biodiversity-authority-releases-rs-15-52-crore-abs-proceeds-from-mustar-2298712" class="px-3 py-1.5 rounded-lg bg-pib-700 hover:bg-pib-800 text-white font-bold text-xs shadow-xs transition-all flex items-center gap-1.5">
                <span>Read Full Dispatch</span>
                <span>→</span>
              </a>
            </div>
          </div>

        </div>

        <!-- RIGHT: Compact River Feed (7 cols) -->
        <div class="lg:col-span-7 flex flex-col space-y-2.5" id="river-stories-container">
          <!-- Populated dynamically via JS: 5 companion stories per page with click-to-preview -->
        </div>

      </div>

      <!-- VIEW 2: COMPACT GRID VIEW (Hidden by default, toggled via switcher) -->
      <div id="releases-grid-view" class="hidden grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <!-- Populated dynamically via JS -->
      </div>

      <!-- COMPACT INTEGRATED PAGINATION BAR (Positioned directly below the split view for zero-scroll visibility!) -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pt-3 border-t border-slate-200 dark:border-zinc-800">
        <div class="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-zinc-400">
          <span id="pagination-summary">Showing releases 1–6 of 15 (Page 1 of 3)</span>
        </div>
        
        <!-- Controls: Prev, Numbered Pills, Next -->
        <div class="flex items-center gap-2" role="navigation" aria-label="Press releases pagination">
          <button id="btn-rel-prev" class="px-3.5 py-1.5 rounded-xl border border-slate-300 dark:border-zinc-700 font-bold text-xs text-slate-600 dark:text-zinc-300 hover:bg-slate-100 dark:hover:bg-zinc-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all" disabled>
            ← Previous
          </button>
          
          <div class="flex items-center gap-1.5" id="pagination-pills-container">
            <button class="page-num-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-pib-700 text-white shadow-xs" data-page="1">1</button>
            <button class="page-num-btn px-3 py-1.5 rounded-xl text-xs font-bold text-slate-600 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-800 transition-colors" data-page="2">2</button>
            <button class="page-num-btn px-3 py-1.5 rounded-xl text-xs font-bold text-slate-600 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-800 transition-colors" data-page="3">3</button>
          </div>

          <button id="btn-rel-next" class="px-3.5 py-1.5 rounded-xl border border-slate-300 dark:border-zinc-700 font-bold text-xs text-slate-600 dark:text-zinc-300 hover:bg-slate-100 dark:hover:bg-zinc-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all">
            Next →
          </button>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: LATEST EXPLAINERS (c4)          -->
    <!-- ========================================== -->
    <section id="explainers" aria-label="Explainers and Factsheets" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex items-end justify-between pb-3 border-b-2 border-emerald-600 dark:border-emerald-500">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-emerald-600 rounded-full"></span>
            <span>Policy Deconstructed</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Latest Explainers</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| नवीनतम व्याख्याता</span>
          </h2>
        </div>
        <div class="flex items-center gap-3">
          <a href="/del/en/explainers" class="text-xs font-bold text-emerald-700 dark:text-emerald-400 hover:underline">
            View All Explainers →
          </a>
        </div>
      </div>

      <!-- Category Filter Tabs (from old.html) -->
      <div class="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-1" id="explainers-filter-tabs">
        <button class="explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-emerald-700 text-white shadow-xs whitespace-nowrap" data-filter="all">All</button>
        <button class="explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-colors whitespace-nowrap" data-filter="Features">Features</button>
        <button class="explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-colors whitespace-nowrap" data-filter="Backgrounders">Backgrounders</button>
        <button class="explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-colors whitespace-nowrap" data-filter="FAQs">FAQs</button>
        <button class="explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-colors whitespace-nowrap" data-filter="Factsheets">Factsheets</button>
      </div>

      <!-- Explainers Reel (All 8 Authentic Items) -->
      <div class="relative">
        <!-- Scroll Buttons -->
        <button id="btn-scroll-explainers-left" class="absolute -left-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 rounded-full bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 shadow-md flex items-center justify-center text-slate-700 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-700 transition-all" aria-label="Scroll explainers left">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        <button id="btn-scroll-explainers-right" class="absolute -right-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 rounded-full bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 shadow-md flex items-center justify-center text-slate-700 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-700 transition-all" aria-label="Scroll explainers right">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>

        <div id="explainers-carousel" class="flex gap-4 overflow-x-auto scrollbar-none scroll-smooth py-2 px-1">
""")

    for exp in explainers_data:
        badge_bg = "bg-emerald-600 text-white" if exp["badge"] == "Factsheet" else "bg-amber-600 text-white"
        img_class = "w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" if exp["is_photo"] else "w-16 h-16 sm:w-20 sm:h-20 object-contain p-2 group-hover:scale-105 transition-transform duration-300"
        bg_card_thumb = "bg-slate-100 dark:bg-zinc-800" if exp["is_photo"] else "bg-gradient-to-br from-slate-50 to-slate-100 dark:from-zinc-800 dark:to-zinc-900"
        parts.append(f"""
          <article class="explainer-card w-64 sm:w-72 shrink-0 bg-white dark:bg-zinc-900 rounded-2xl border border-slate-200 dark:border-zinc-800 shadow-xs hover:shadow-md transition-all overflow-hidden flex flex-col justify-between group" data-badge="{exp['badge']}">
            <!-- Top Visual Frame (16:9 Thumbnail) -->
            <a href="{exp['url']}" class="relative w-full aspect-video {bg_card_thumb} border-b border-slate-100 dark:border-zinc-800 flex items-center justify-center overflow-hidden block">
              <img src="{exp['img']}" alt="{html.escape(exp['title'])}" class="{img_class}" loading="lazy">
              <!-- Top-Right Badge -->
              <span class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-bold {badge_bg} shadow-xs tracking-wide">
                {exp['badge']}
              </span>
              <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent pointer-events-none"></div>
            </a>

            <!-- Card Body -->
            <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between gap-2 mb-1.5">
                  <span class="text-[11px] font-bold text-emerald-700 dark:text-emerald-400 uppercase tracking-wider truncate">
                    {exp['category']}
                  </span>
                  <span class="text-[10px] text-slate-400 font-mono shrink-0">
                    {exp['date']}
                  </span>
                </div>
                <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors line-clamp-2">
                  <a href="{exp['url']}">
                    {html.escape(exp['title'])}
                  </a>
                </h3>
                <p class="text-xs text-slate-600 dark:text-zinc-400 mt-2 line-clamp-2 leading-relaxed">
                  {html.escape(exp['desc'])}
                </p>
              </div>
              <div class="mt-4 pt-3 border-t border-slate-100 dark:border-zinc-800 flex items-center justify-between">
                <span class="text-[11px] text-slate-400 font-mono">PIB {exp['badge']}</span>
                <a href="{exp['url']}" class="text-xs font-bold text-emerald-700 dark:text-emerald-400 hover:underline flex items-center gap-1">
                  <span>Read Full Explainer</span>
                  <span>→</span>
                </a>
              </div>
            </div>
          </article>
        """)

    parts.append("""
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: MEDIA DESK & LIVE ADVISORIES    -->
    <!-- ========================================== -->
    <section id="media-desk" aria-label="Media Desk & Advisories" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 pb-3 border-b-2 border-amber-500">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-amber-600 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-amber-500 rounded-full"></span>
            <span>Accredited Press & Broadcasters</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Media Desk</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| मीडिया डेस्क</span>
          </h2>
        </div>

        <!-- Tab Switcher -->
        <div class="flex items-center gap-1 bg-slate-200/80 dark:bg-zinc-800 p-1 rounded-xl" role="tablist">
          <button id="tab-media-advisory" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white dark:bg-zinc-700 text-slate-900 dark:text-white shadow-xs" role="tab" aria-selected="true">
            Live Advisories (3)
          </button>
          <button id="tab-media-services" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-slate-900" role="tab" aria-selected="false">
            Accreditation &amp; Services
          </button>
        </div>
      </div>

      <!-- Tab 1: Advisories Grid -->
      <div id="panel-media-advisory" class="grid grid-cols-1 md:grid-cols-3 gap-5" role="tabpanel">
    """)

    for adv in advisories_data:
        parts.append(f"""
        <article class="bg-amber-50/50 dark:bg-amber-950/20 rounded-2xl p-5 border border-amber-200 dark:border-amber-900/60 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500 text-slate-950 uppercase tracking-wider">
                <span class="w-1.5 h-1.5 rounded-full bg-slate-950 pulse-live"></span>
                <span>Cabinet Briefing</span>
              </span>
              <span class="text-xs font-mono font-semibold text-amber-800 dark:text-amber-400">{adv['date']}</span>
            </div>

            <h3 class="text-sm font-bold text-slate-900 dark:text-zinc-100 leading-snug">
              <a href="{adv['url']}" class="hover:underline">
                {html.escape(adv['title'])}
              </a>
            </h3>

            <div class="mt-3 space-y-1.5 text-xs text-slate-700 dark:text-zinc-300">
              <div class="flex items-start gap-1.5">
                <svg class="w-4 h-4 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <span class="font-semibold">{adv['time']}</span>
              </div>
              <div class="flex items-start gap-1.5">
                <svg class="w-4 h-4 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                <span>{adv['venue']}</span>
              </div>
              <div class="flex items-start gap-1.5 text-[11px] text-amber-900 dark:text-amber-300 font-medium bg-amber-100/60 dark:bg-amber-900/40 p-1.5 rounded">
                <span>⚠️ {adv['req']}</span>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-amber-200/60 dark:border-amber-900/40 flex items-center justify-between text-xs">
            <span class="text-slate-500 font-medium">PIB Media Advisory</span>
            <a href="{adv['url']}" class="font-bold text-amber-800 dark:text-amber-400 hover:underline">Full Advisory →</a>
          </div>
        </article>
        """)

    parts.append(f"""
      </div>

      <!-- Tab 2: Services Grid (Hidden by default) -->
      <div id="panel-media-services" class="hidden grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5" role="tabpanel">
        
        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-pib-100 dark:bg-zinc-800 text-pib-700 dark:text-blue-400 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"></path></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">Press Accreditation</h3>
            <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1">Apply for fresh PIB card, renewal, and category changes under Central Press Accreditation Rules.</p>
          </div>
          <a href="/del/en/accreditation" class="mt-4 text-xs font-bold text-pib-700 dark:text-blue-400 hover:underline">Access Portal →</a>
        </div>

        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-amber-100 dark:bg-zinc-800 text-amber-700 dark:text-amber-400 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">Media Invitations</h3>
            <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1">RSVP to bilateral summits, national day celebrations, and state banquet media enclosures.</p>
          </div>
          <a href="/del/en/media-invitations" class="mt-4 text-xs font-bold text-amber-700 dark:text-amber-400 hover:underline">Check Invitations →</a>
        </div>

        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-zinc-800 text-emerald-700 dark:text-emerald-400 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">NMC Facilitation</h3>
            <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1">Book press conference halls, editing suites, satellite uplinks, and briefing lounges at NMC.</p>
          </div>
          <a href="/del/en/media-facilitation" class="mt-4 text-xs font-bold text-emerald-700 dark:text-emerald-400 hover:underline">Book Facilities →</a>
        </div>

        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-purple-100 dark:bg-zinc-800 text-purple-700 dark:text-purple-400 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"></path></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">All Announcements</h3>
            <p class="text-xs text-slate-600 dark:text-zinc-400 mt-1">Search historical archive of all advisories, media alerts, and embargo notices.</p>
          </div>
          <a href="/del/en/media-announcements" class="mt-4 text-xs font-bold text-purple-700 dark:text-purple-400 hover:underline">Browse Repository →</a>
        </div>

      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: PIB FACT CHECK UNIT BANNER      -->
    <!-- ========================================== -->
    <section id="fact-check" aria-label="PIB Fact Check Unit" class="scroll-mt-24">
      <div class="bg-gradient-to-r from-pib-900 via-pib-700 to-pib-800 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden">
        
        <div class="absolute right-0 bottom-0 translate-x-12 translate-y-12 opacity-10 pointer-events-none">
          <svg class="w-96 h-96" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
        </div>

        <div class="relative z-10 max-w-3xl">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-400 text-pib-900 font-bold text-xs uppercase tracking-wider mb-3">
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
            <span>Verified Official Information</span>
          </div>

          <h2 class="text-2xl sm:text-3xl font-bold tracking-tight mb-2">
            Spotted a viral rumour? Verify with PIB Fact Check
          </h2>
          <p class="text-sm sm:text-base text-slate-200 leading-relaxed mb-6">
            The PIB Fact Check Unit monitors and debunks fake news, misleading claims, and impersonation regarding Government of India policies, schemes, and official notifications.
          </p>

          <div class="flex flex-wrap items-center gap-4">
            <a href="https://wa.me/918799711259" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm shadow-md transition-all">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
              <span>WhatsApp: +91 87997 11259</span>
            </a>

            <a href="mailto:pibfactcheck@gmail.com" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs sm:text-sm border border-white/20 transition-all">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              <span>pibfactcheck@gmail.com</span>
            </a>

            <a href="/del/en/fact-check-unit" class="text-xs sm:text-sm font-bold text-amber-300 hover:text-amber-200 underline ml-auto">
              Browse Fact Check Registry →
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: PIB VIDEOS THEATER (c6)         -->
    <!-- ========================================== -->
    <section id="videos" aria-label="PIB Videos" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex items-end justify-between pb-3 border-b-2 border-red-600">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-red-600 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-red-600 rounded-full"></span>
            <span>Broadcasts & Briefings</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>PIB Videos</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| पीआईबी वीडियो</span>
          </h2>
        </div>
        <a href="/del/en/galleries?tab=videos" class="text-xs font-bold text-red-600 dark:text-red-400 hover:underline">
          View All Videos →
        </a>
      </div>

      <!-- Video Theater Layout: Large Player + Playlist -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        <!-- Left: Featured Video Player (8 cols) -->
        <div class="lg:col-span-8 bg-black rounded-2xl overflow-hidden shadow-lg border border-slate-200 dark:border-zinc-800">
          <div class="relative aspect-video w-full group cursor-pointer" id="main-video-player">
            <img id="main-video-thumbnail" src="{videos_data[0]['img']}" alt="{html.escape(videos_data[0]['title'])}" class="w-full h-full object-cover">
            
            <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 flex items-center justify-center transition-all">
              <div class="w-16 h-16 sm:w-20 sm:h-20 rounded-full bg-red-600 text-white flex items-center justify-center shadow-2xl group-hover:scale-110 transition-transform">
                <svg class="w-8 h-8 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>

            <span id="main-video-duration" class="absolute bottom-4 right-4 px-2.5 py-1 rounded bg-black/80 backdrop-blur-sm text-xs font-mono font-bold text-white">
              {videos_data[0]['duration']}
            </span>
          </div>

          <div class="p-5 bg-zinc-900 text-white">
            <div class="flex items-center gap-2 mb-2">
              <span id="main-video-tag" class="px-2 py-0.5 rounded text-[11px] font-bold bg-red-600 text-white uppercase tracking-wider">
                {videos_data[0]['tag']}
              </span>
              <span id="main-video-date" class="text-xs text-zinc-400 font-mono">
                {videos_data[0]['date']}
              </span>
            </div>
            <h3 id="main-video-title" class="text-base sm:text-lg font-bold leading-snug">
              {videos_data[0]['title']}
            </h3>
          </div>
        </div>

        <!-- Right: Scrollable Playlist (4 cols - All 10 Authentic Videos) -->
        <div class="lg:col-span-4 bg-white dark:bg-zinc-900 rounded-2xl p-4 border border-slate-200 dark:border-zinc-800 shadow-xs flex flex-col h-[460px] sm:h-[500px]">
          <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-zinc-800">
            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-zinc-400">
              Briefings Playlist ({len(videos_data)})
            </h3>
            <span class="text-[11px] text-red-600 font-semibold">Click to play</span>
          </div>

          <div class="flex-1 overflow-y-auto space-y-2 pr-1" id="video-playlist-container">
    """)

    for i, v in enumerate(videos_data):
        active_border = "border-red-600 bg-red-50/50 dark:bg-zinc-800" if i == 0 else "border-transparent hover:bg-slate-50 dark:hover:bg-zinc-800/60"
        parts.append(f"""
            <button class="video-playlist-item w-full text-left p-2 rounded-xl border {active_border} flex items-center gap-3 transition-all group" 
                    data-video-index="{i}"
                    data-img="{v['img']}"
                    data-title="{html.escape(v['title'])}"
                    data-date="{v['date']}"
                    data-tag="{v['tag']}"
                    data-duration="{v['duration']}">
              <div class="relative w-20 h-12 rounded-lg overflow-hidden shrink-0 bg-black">
                <img src="{v['img']}" alt="{html.escape(v['title'])}" class="w-full h-full object-cover">
                <span class="absolute bottom-1 right-1 px-1 rounded bg-black/80 text-[9px] font-mono text-white leading-tight">
                  {v['duration']}
                </span>
              </div>
              <div class="flex-1 min-w-0">
                <h4 class="text-xs font-bold text-slate-800 dark:text-zinc-200 line-clamp-2 leading-snug group-hover:text-red-600 dark:group-hover:text-red-400 transition-colors">
                  {html.escape(v['title'])}
                </h4>
                <span class="text-[10px] text-slate-400 font-mono mt-0.5 block">{v['date']}</span>
              </div>
            </button>
        """)

    parts.append(f"""
          </div>
        </div>

      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 7: PHOTO GALLERY (c7)              -->
    <!-- ========================================== -->
    <section id="photos" aria-label="Photo Gallery" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex items-end justify-between pb-3 border-b-2 border-indigo-600">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-indigo-600 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-indigo-600 rounded-full"></span>
            <span>Visual Chronicles</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Photo Gallery</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| चित्र दीर्घा</span>
          </h2>
        </div>
        <a href="/del/en/galleries?tab=photos" class="text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:underline">
          View All Photos →
        </a>
      </div>

      <!-- Featured Photo Display + Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
        
        <!-- Large Featured Photo (7 cols) -->
        <div class="lg:col-span-7 bg-white dark:bg-zinc-900 rounded-2xl overflow-hidden border border-slate-200 dark:border-zinc-800 shadow-sm flex flex-col">
          <div class="relative aspect-video w-full bg-slate-900 cursor-pointer group" id="featured-photo-wrapper" data-photo-index="0">
            <img id="featured-photo-img" src="{photos_data[0]['img']}" alt="{html.escape(photos_data[0]['caption'])}" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/0 transition-colors"></div>
            <span class="absolute top-3 left-3 px-2.5 py-1 rounded-md bg-black/70 backdrop-blur-sm text-white text-xs font-semibold">
              Featured Coverage
            </span>
            <button class="absolute bottom-3 right-3 p-2 rounded-full bg-black/70 hover:bg-black text-white text-xs backdrop-blur-sm transition-all" title="View full screen">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-5h-4m4 0v4m0-4l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
            </button>
          </div>
          <div class="p-5 flex flex-col justify-between flex-1">
            <p id="featured-photo-caption" class="text-sm sm:text-base font-medium text-slate-800 dark:text-zinc-200 leading-snug">
              {photos_data[0]['caption']}
            </p>
            <div class="mt-4 pt-3 border-t border-slate-100 dark:border-zinc-800 flex items-center justify-between text-xs text-slate-400">
              <span id="featured-photo-loc">{photos_data[0]['location']}</span>
              <span id="featured-photo-date" class="font-mono">{photos_data[0]['date']}</span>
            </div>
          </div>
        </div>

        <!-- Right: 9-Photo Interactive Thumbnail Grid (5 cols) -->
        <div class="lg:col-span-5 bg-white dark:bg-zinc-900 rounded-2xl p-4 border border-slate-200 dark:border-zinc-800 shadow-sm flex flex-col">
          <div class="flex items-center justify-between pb-2 mb-3 border-b border-slate-100 dark:border-zinc-800">
            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Event Highlights</span>
            <span class="text-[11px] text-indigo-600 font-semibold">Click to preview</span>
          </div>

          <div class="grid grid-cols-3 gap-2.5 flex-1">
    """)

    for i, p in enumerate(photos_data[1:], 1):
        parts.append(f"""
            <button class="photo-thumb-btn relative rounded-xl overflow-hidden aspect-square bg-slate-100 dark:bg-zinc-800 group focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    data-photo-index="{i}"
                    data-img="{p['img']}"
                    data-caption="{html.escape(p['caption'])}"
                    data-location="{p['location']}"
                    data-date="{p['date']}">
              <img src="{p['img']}" alt="{html.escape(p['caption'])}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300">
              <div class="absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors"></div>
            </button>
        """)

    parts.append("""
          </div>
        </div>

      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 8: BLOGS & FEATURES (c8)           -->
    <!-- ========================================== -->
    <section id="blogs" aria-label="Blogs and Special Features" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex items-end justify-between pb-3 border-b-2 border-teal-600">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-teal-600 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-teal-600 rounded-full"></span>
            <span>In-depth Perspectives</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Special Features &amp; Blogs</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| विशेष आलेख</span>
          </h2>
        </div>
        <a href="/del/en/blogs" class="text-xs font-bold text-teal-600 dark:text-teal-400 hover:underline">
          View All Blogs (12) →
        </a>
      </div>

      <!-- Blogs Reel with Horizontal Scroll & Show More -->
      <div class="relative">
        <!-- Scroll Buttons -->
        <button id="btn-scroll-blogs-left" class="absolute -left-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 rounded-full bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 shadow-md flex items-center justify-center text-slate-700 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-700 transition-all" aria-label="Scroll blogs left">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        <button id="btn-scroll-blogs-right" class="absolute -right-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 rounded-full bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 shadow-md flex items-center justify-center text-slate-700 dark:text-zinc-200 hover:bg-slate-100 dark:hover:bg-zinc-700 transition-all" aria-label="Scroll blogs right">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </button>

        <div id="blogs-carousel" class="flex gap-4 sm:gap-5 overflow-x-auto scrollbar-none scroll-smooth py-2 px-1">
    """)

    for b in blogs_data:
        parts.append(f"""
          <article class="w-64 sm:w-72 shrink-0 bg-white dark:bg-zinc-900 rounded-2xl overflow-hidden border border-slate-200 dark:border-zinc-800 shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <!-- Blog Thumbnail -->
              <div class="relative aspect-video w-full bg-slate-100 dark:bg-zinc-800 overflow-hidden">
                <img src="{b['img']}" alt="{html.escape(b['title'])}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded text-[10px] font-bold bg-black/70 backdrop-blur-xs text-white">
                  {b['tag']}
                </span>
              </div>

              <!-- Blog Info -->
              <div class="p-4">
                <div class="text-[11px] text-slate-400 font-mono mb-1">{b['date']}</div>
                <h3 class="text-sm font-bold text-slate-900 dark:text-white leading-snug group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors line-clamp-2">
                  <a href="{b['url']}">
                    {html.escape(b['title'])}
                  </a>
                </h3>
                <p class="text-xs text-slate-600 dark:text-zinc-400 mt-2 line-clamp-3 leading-relaxed">
                  {html.escape(b['desc'])}
                </p>
              </div>
            </div>

            <div class="px-4 pb-4 pt-2 flex items-center justify-between text-xs border-t border-slate-100 dark:border-zinc-800/80">
              <span class="text-slate-400 font-medium">PIB Feature</span>
              <a href="{b['url']}" class="font-bold text-teal-600 dark:text-teal-400 hover:underline">Read Article →</a>
            </div>
          </article>
        """)

    parts.append(f"""
          <!-- Trailing Show More Card -->
          <a href="/del/en/blogs" class="w-64 sm:w-72 shrink-0 bg-gradient-to-br from-slate-50 via-teal-50/40 to-white dark:from-zinc-900 dark:via-teal-950/20 dark:to-zinc-900 rounded-2xl border-2 border-dashed border-teal-300 dark:border-teal-700/80 hover:border-teal-600 dark:hover:border-teal-400 transition-all p-6 flex flex-col items-center justify-center text-center group cursor-pointer shadow-xs hover:shadow-md">
            <div class="w-14 h-14 rounded-full bg-teal-100 dark:bg-teal-900/50 text-teal-700 dark:text-teal-300 flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </div>
            <span class="text-base font-bold text-slate-900 dark:text-white group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors">View All Blogs</span>
            <span class="text-xs text-slate-500 dark:text-zinc-400 mt-1 max-w-[200px]">Explore all 12 special features &amp; perspectives</span>
            <span class="mt-4 px-4 py-2 rounded-xl bg-teal-600 text-white font-bold text-xs shadow-xs group-hover:bg-teal-700 transition-colors flex items-center gap-1.5">
              <span>Show More</span>
              <span>→</span>
            </span>
          </a>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 9: REGIONAL OFFICES & DIRECTORY    -->
    <!-- ========================================== -->
    <section id="directory" aria-label="Regional Offices & RTI Directory" class="scroll-mt-24 space-y-6">
      
      <!-- Section Header -->
      <div class="flex items-end justify-between pb-3 border-b-2 border-slate-700 dark:border-zinc-600">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-slate-600 dark:text-zinc-400 uppercase tracking-wider mb-1">
            <span class="w-2.5 h-1 bg-slate-600 rounded-full"></span>
            <span>Nationwide Network</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <span>Regional Offices &amp; RTI</span>
            <span class="text-slate-400 font-normal text-lg sm:text-xl">| क्षेत्रीय कार्यालय एवं आरटीआई</span>
          </h2>
        </div>
        <a href="/del/en/regional-offices" class="text-xs font-bold text-pib-700 dark:text-blue-400 hover:underline">
          All 34 Regional Hubs →
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Column 1: Regional Offices -->
        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs">
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-slate-100 dark:border-zinc-800">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            <h3 class="font-bold text-sm text-slate-900 dark:text-white uppercase tracking-wider">Regional Networks</h3>
          </div>
          <ul class="space-y-2.5 text-xs text-slate-700 dark:text-zinc-300">
            <li class="flex items-center justify-between">
              <span class="font-semibold">Northern Region:</span>
              <span class="text-slate-500">Delhi, Chandigarh, Srinagar, Jammu</span>
            </li>
            <li class="flex items-center justify-between">
              <span class="font-semibold">Western Region:</span>
              <span class="text-slate-500">Mumbai, Ahmedabad, Pune, Panaji</span>
            </li>
            <li class="flex items-center justify-between">
              <span class="font-semibold">Southern Region:</span>
              <span class="text-slate-500">Chennai, Hyderabad, Bengaluru, Kochi</span>
            </li>
            <li class="flex items-center justify-between">
              <span class="font-semibold">Eastern Region:</span>
              <span class="text-slate-500">Kolkata, Bhubaneswar, Patna, Ranchi</span>
            </li>
            <li class="flex items-center justify-between">
              <span class="font-semibold">North-Eastern:</span>
              <span class="text-slate-500">Guwahati, Shillong, Imphal, Agartala</span>
            </li>
          </ul>
          <a href="/del/en/regional-offices" class="mt-4 inline-block text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline">
            View Complete Directory &amp; Phonebook →
          </a>
        </div>

        <!-- Column 2: RTI & Contact Us -->
        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs">
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-slate-100 dark:border-zinc-800">
            <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
            <h3 class="font-bold text-sm text-slate-900 dark:text-white uppercase tracking-wider">RTI &amp; Grievances</h3>
          </div>
          <div class="space-y-2 text-xs text-slate-700 dark:text-zinc-300">
            <p><strong>Nodal RTI Officer:</strong> Shri Rajeev Kumar, Director</p>
            <p><strong>Appellate Authority:</strong> Additional Director General (Coordination)</p>
            <p><strong>Headquarters:</strong> National Media Centre, 7E Raisina Road, New Delhi - 110001</p>
            <p><strong>Media Inquiries:</strong> feedback.pib@gov.in</p>
          </div>
          <a href="/del/en/rti-contact" class="mt-4 inline-block text-xs font-bold text-emerald-600 dark:text-emerald-400 hover:underline">
            Submit RTI Application Online →
          </a>
        </div>

        <!-- Column 3: National Government Portals -->
        <div class="bg-white dark:bg-zinc-900 rounded-2xl p-5 border border-slate-200 dark:border-zinc-800 shadow-xs">
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-slate-100 dark:border-zinc-800">
            <span class="w-2 h-2 rounded-full bg-amber-500"></span>
            <h3 class="font-bold text-sm text-slate-900 dark:text-white uppercase tracking-wider">National Portals</h3>
          </div>
          <ul class="space-y-2 text-xs">
            <li><a href="https://www.india.gov.in" target="_blank" rel="noopener noreferrer" class="text-slate-700 dark:text-zinc-300 hover:text-pib-700 font-medium flex items-center justify-between"><span>India.gov.in (National Portal)</span><span>↗</span></a></li>
            <li><a href="https://mygov.in" target="_blank" rel="noopener noreferrer" class="text-slate-700 dark:text-zinc-300 hover:text-pib-700 font-medium flex items-center justify-between"><span>MyGov.in (Citizen Engagement)</span><span>↗</span></a></li>
            <li><a href="https://data.gov.in" target="_blank" rel="noopener noreferrer" class="text-slate-700 dark:text-zinc-300 hover:text-pib-700 font-medium flex items-center justify-between"><span>Data.gov.in (Open Government Data)</span><span>↗</span></a></li>
            <li><a href="https://www.digitalindia.gov.in" target="_blank" rel="noopener noreferrer" class="text-slate-700 dark:text-zinc-300 hover:text-pib-700 font-medium flex items-center justify-between"><span>Digital India Portal</span><span>↗</span></a></li>
          </ul>
          <a href="/del/en/government-links" class="mt-4 inline-block text-xs font-bold text-amber-600 hover:underline">
            All Government Links →
          </a>
        </div>

      </div>

    </section>

  </main>

  <!-- ========================================== -->
  <!-- PHOTO LIGHTBOX MODAL (ACCESSIBLE)          -->
  <!-- ========================================== -->
  <div id="photo-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden items-center justify-center p-4" role="dialog" aria-modal="true" aria-labelledby="modal-caption">
    <div class="relative max-w-5xl w-full bg-zinc-900 rounded-2xl overflow-hidden border border-zinc-800 flex flex-col max-h-[90vh]">
      <button id="btn-modal-close" class="absolute top-4 right-4 z-10 p-2 rounded-full bg-black/60 hover:bg-black text-white transition-all" aria-label="Close modal">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
      <div class="relative w-full h-[60vh] bg-black flex items-center justify-center">
        <img id="modal-img" src="{photos_data[0]['img']}" alt="" class="max-h-full max-w-full object-contain">
      </div>
      <div class="p-5 bg-zinc-900 text-white border-t border-zinc-800 overflow-y-auto">
        <p id="modal-caption" class="text-sm sm:text-base font-medium leading-snug"></p>
        <div class="mt-3 flex items-center justify-between text-xs text-zinc-400">
          <span id="modal-loc"></span>
          <span id="modal-date" class="font-mono"></span>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- COMPREHENSIVE GOVERNMENT FOOTER            -->
  <!-- ========================================== -->
  <footer class="bg-pib-900 text-white mt-16 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-12 space-y-10">
      
      <!-- Tier 1: Quick Links and Directory Navigation -->
      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6 text-xs">
        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">News &amp; Media</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/press-releases" class="hover:text-white hover:underline">Press Releases</a></li>
            <li><a href="/del/en/press-notes" class="hover:text-white hover:underline">Press Notes</a></li>
            <li><a href="/del/en/pibtv" class="hover:text-white hover:underline">PIB TV</a></li>
            <li><a href="/del/en/galleries?tab=videos" class="hover:text-white hover:underline">Video Broadcasts</a></li>
            <li><a href="/del/en/galleries?tab=photos" class="hover:text-white hover:underline">Photo Gallery</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">Media Services</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/accreditation" class="hover:text-white hover:underline">Accreditation Portal</a></li>
            <li><a href="/del/en/media-invitations" class="hover:text-white hover:underline">Media Invitations</a></li>
            <li><a href="/del/en/media-facilitation" class="hover:text-white hover:underline">Media Facilitation</a></li>
            <li><a href="/del/en/media-announcements" class="hover:text-white hover:underline">Advisories &amp; Alerts</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">Knowledge Base</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/explainers" class="hover:text-white hover:underline">Policy Explainers</a></li>
            <li><a href="/del/en/blogs" class="hover:text-white hover:underline">Special Blogs</a></li>
            <li><a href="/del/en/archives" class="hover:text-white hover:underline">Historical Archives</a></li>
            <li><a href="/del/en/fact-check-unit" class="hover:text-white hover:underline">Fact Check Unit</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">Governance</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/ministries" class="hover:text-white hover:underline">Ministries Directory</a></li>
            <li><a href="/del/en/regional-offices" class="hover:text-white hover:underline">Regional Hubs</a></li>
            <li><a href="/del/en/rti-contact" class="hover:text-white hover:underline">RTI Cell</a></li>
            <li><a href="/del/en/government-links" class="hover:text-white hover:underline">Government Portals</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">Mandatory Policies</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/terms-and-conditions" class="hover:text-white hover:underline">Terms &amp; Conditions</a></li>
            <li><a href="/del/en/privacy-policy" class="hover:text-white hover:underline">Privacy Policy</a></li>
            <li><a href="/del/en/copyright-policy" class="hover:text-white hover:underline">Copyright Policy</a></li>
            <li><a href="/del/en/hyperlinking-policy" class="hover:text-white hover:underline">Hyperlinking Policy</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold text-amber-400 uppercase tracking-wider mb-3">Citizen Support</h4>
          <ul class="space-y-2 text-white/80">
            <li><a href="/del/en/help" class="hover:text-white hover:underline">Help &amp; FAQs</a></li>
            <li><a href="https://pib.gov.in/feedback" target="_blank" rel="noopener noreferrer" class="hover:text-white hover:underline">Feedback (External) ↗</a></li>
            <li><a href="#" id="footer-cookie-btn" class="hover:text-white hover:underline">Cookie Settings</a></li>
            <li><a href="DBIM3.0.pdf" target="_blank" class="hover:text-white hover:underline">STQC Certificate (PDF) ↗</a></li>
          </ul>
        </div>
      </div>

      <!-- Tier 2: Standards & Compliance Badges -->
      <div class="pt-8 border-t border-white/10 flex flex-wrap items-center justify-between gap-4 text-xs text-white/70">
        <div class="flex items-center gap-4 flex-wrap">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded bg-white/10 border border-white/15">
            <svg class="w-4 h-4 text-emerald-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
            <span>DPDP Act 2023 Compliant</span>
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded bg-white/10 border border-white/15">
            <svg class="w-4 h-4 text-blue-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
            <span>GIGW 3.0 / DBIM Certified</span>
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded bg-white/10 border border-white/15">
            <span>STQC Web Quality Certified</span>
          </span>
        </div>

        <div class="text-right text-[11px]">
          <span>Page Last Updated: <strong>13 August 2026</strong></span>
          <span class="mx-2 text-white/30">|</span>
          <span>Visitors: <strong>42,891,045</strong></span>
        </div>
      </div>

      <!-- Tier 3: Official Copyright & Attribution -->
      <div class="pt-6 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-white/60">
        <p>© 2026 Press Information Bureau, Government of India. All rights reserved.</p>
        <p>Designed, Developed &amp; Hosted by <strong>National Informatics Centre (NIC)</strong></p>
      </div>

    </div>
  </footer>

  <!-- FLOATING BACK TO TOP BUTTON -->
  <button id="btn-back-to-top" class="fixed bottom-6 right-6 z-40 w-11 h-11 rounded-full bg-pib-700 hover:bg-pib-800 text-white shadow-xl border border-white/30 hidden items-center justify-center transition-all hover:scale-110 focus:outline-none focus:ring-2 focus:ring-amber-400" title="Back to top" aria-label="Back to top of page">
    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
  </button>

  <!-- COOKIE CONSENT BANNER (DPDP ACT 2023) -->
  <div id="cookie-banner" class="fixed bottom-0 inset-x-0 z-50 bg-slate-900/95 text-white p-4 sm:p-5 border-t border-white/20 backdrop-blur-md shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-4" role="region" aria-label="Cookie Preferences">
    <div class="text-xs sm:text-sm text-slate-200 max-w-4xl">
      We use cookies to enhance website navigation, analyze visitor traffic, and ensure accessibility compliance under the <strong>Digital Personal Data Protection Act, 2023</strong>. By continuing, you agree to our <a href="/del/en/privacy-policy" class="text-amber-400 underline">Privacy Policy</a>.
    </div>
    <div class="flex items-center gap-3 shrink-0">
      <button id="btn-cookie-accept" class="px-4 py-2 rounded-lg bg-amber-500 hover:bg-amber-600 text-pib-900 font-bold text-xs transition-colors">
        Accept All
      </button>
      <button id="btn-cookie-dismiss" class="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-white text-xs border border-white/20 transition-colors">
        Close
      </button>
    </div>
  </div>
""")

    # CLIENT-SIDE JAVASCRIPT (PLAIN RAW STRING CONCATENATION - ZERO BRACE CONFLICTS!)
    js_content = """
  <script>
    (function() {
      // DATA SOURCES
      const slides = """ + slides_json + """;
      const releasesData = """ + releases_json + """;
      const explainers = """ + explainers_json + """;
      const videos = """ + videos_json + """;
      const photos = """ + photos_json + """;
      const blogs = """ + blogs_json + """;

      // 1. CAROUSEL LOGIC
      let currentSlide = 0;
      let slideInterval = null;
      let isPlaying = true;
      const slideElements = document.querySelectorAll('.carousel-slide');
      const dotElements = document.querySelectorAll('.carousel-dot');
      const counterEl = document.getElementById('carousel-counter');
      const pauseBtn = document.getElementById('btn-carousel-pause');
      const playIcon = document.getElementById('carousel-play-icon');
      const pauseIcon = document.getElementById('carousel-pause-icon');

      function showSlide(idx) {
        currentSlide = (idx + slides.length) % slides.length;
        slideElements.forEach((el, i) => {
          if (i === currentSlide) {
            el.classList.remove('opacity-0', 'z-0', 'pointer-events-none');
            el.classList.add('opacity-100', 'z-10');
          } else {
            el.classList.add('opacity-0', 'z-0', 'pointer-events-none');
            el.classList.remove('opacity-100', 'z-10');
          }
        });
        dotElements.forEach((dot, i) => {
          if (i === currentSlide) {
            dot.className = "carousel-dot h-2.5 rounded-full transition-all duration-300 bg-pib-700 dark:bg-amber-400 w-8";
            dot.setAttribute('aria-selected', 'true');
          } else {
            dot.className = "carousel-dot h-2.5 rounded-full transition-all duration-300 bg-slate-300 dark:bg-zinc-700 w-2.5";
            dot.setAttribute('aria-selected', 'false');
          }
        });
        if (counterEl) counterEl.textContent = `${currentSlide + 1} / ${slides.length}`;
      }

      function nextSlide() { showSlide(currentSlide + 1); }
      function prevSlide() { showSlide(currentSlide - 1); }

      function startCarousel() {
        stopCarousel();
        slideInterval = setInterval(nextSlide, 5000);
        isPlaying = true;
        if (playIcon) playIcon.classList.add('hidden');
        if (pauseIcon) pauseIcon.classList.remove('hidden');
      }

      function stopCarousel() {
        if (slideInterval) clearInterval(slideInterval);
        isPlaying = false;
        if (playIcon) playIcon.classList.remove('hidden');
        if (pauseIcon) pauseIcon.classList.add('hidden');
      }

      const btnPrev = document.getElementById('btn-carousel-prev');
      const btnNext = document.getElementById('btn-carousel-next');
      if (btnPrev) btnPrev.addEventListener('click', () => { prevSlide(); if (isPlaying) startCarousel(); });
      if (btnNext) btnNext.addEventListener('click', () => { nextSlide(); if (isPlaying) startCarousel(); });
      if (pauseBtn) pauseBtn.addEventListener('click', () => { isPlaying ? stopCarousel() : startCarousel(); });

      dotElements.forEach(dot => {
        dot.addEventListener('click', () => {
          const targetIdx = parseInt(dot.getAttribute('data-dot-index'), 10);
          showSlide(targetIdx);
          if (isPlaying) startCarousel();
        });
      });

      // Keyboard arrow control on carousel
      window.addEventListener('keydown', (e) => {
        if (document.activeElement && document.activeElement.tagName === 'INPUT') return;
        if (e.key === 'ArrowRight') nextSlide();
        if (e.key === 'ArrowLeft') prevSlide();
      });

      startCarousel();

      // 2. STICKY NAVBAR READING PROGRESS
      const progressBar = document.getElementById('scroll-progress-bar');
      const backToTopBtn = document.getElementById('btn-back-to-top');

      window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        if (progressBar) progressBar.style.width = progress + '%';

        if (backToTopBtn) {
          if (scrollTop > 400) {
            backToTopBtn.classList.remove('hidden');
            backToTopBtn.classList.add('flex');
          } else {
            backToTopBtn.classList.add('hidden');
            backToTopBtn.classList.remove('flex');
          }
        }
      });

      if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        });
      }

      // 3. FONT RESIZE ADJUSTER
      let currentFontScale = 100;
      const decBtn = document.getElementById('btn-font-dec');
      const resetBtn = document.getElementById('btn-font-reset');
      const incBtn = document.getElementById('btn-font-inc');

      if (decBtn) decBtn.addEventListener('click', () => {
        if (currentFontScale > 85) {
          currentFontScale -= 5;
          document.documentElement.style.fontSize = currentFontScale + '%';
        }
      });
      if (resetBtn) resetBtn.addEventListener('click', () => {
        currentFontScale = 100;
        document.documentElement.style.fontSize = '100%';
      });
      if (incBtn) incBtn.addEventListener('click', () => {
        if (currentFontScale < 125) {
          currentFontScale += 5;
          document.documentElement.style.fontSize = currentFontScale + '%';
        }
      });

      // 4. THEME & CONTRAST TOGGLES
      const themeToggle = document.getElementById('btn-theme-toggle');
      if (themeToggle) {
        themeToggle.addEventListener('click', () => {
          document.documentElement.classList.toggle('dark');
        });
      }

      const contrastBtn = document.getElementById('btn-contrast');
      if (contrastBtn) {
        contrastBtn.addEventListener('click', () => {
          document.documentElement.classList.toggle('high-contrast');
        });
      }

      // 5. ENHANCED PRESS RELEASES: LEAD & RIVER + COMPACT PAGINATION + VIEW SWITCHER
      let currentRelPage = 1;
      const pageSize = 6; // 1 Lead + 5 River companion stories per page
      let activeCategoryTab = 'latest';
      let activeMinistryFilter = '';
      let activeSearchQuery = '';
      let activeViewMode = 'split'; // 'split' or 'grid'

      const riverContainer = document.getElementById('river-stories-container');
      const gridContainer = document.getElementById('releases-grid-view');
      const splitView = document.getElementById('releases-split-view');
      const paginationSummary = document.getElementById('pagination-summary');
      const countBadge = document.getElementById('releases-count-badge');
      const pillsContainer = document.getElementById('pagination-pills-container');
      const btnPrevPage = document.getElementById('btn-rel-prev');
      const btnNextPage = document.getElementById('btn-rel-next');

      // Lead story elements
      const leadTitleLink = document.getElementById('lead-story-title-link');
      const leadMinistry = document.getElementById('lead-story-ministry');
      const leadReadtime = document.getElementById('lead-story-readtime');
      const leadBullets = document.getElementById('lead-story-bullets');
      const leadDate = document.getElementById('lead-story-date');
      const leadCta = document.getElementById('lead-story-cta');
      const leadShare = document.getElementById('lead-story-share');

      function getFilteredReleases() {
        return releasesData.filter(item => {
          if (activeCategoryTab === 'top' && !item.top) return false;
          if (activeCategoryTab === 'mostread' && !item.most_read) return false;

          if (activeMinistryFilter && !item.ministry.toLowerCase().includes(activeMinistryFilter.toLowerCase())) return false;

          if (activeSearchQuery) {
            const q = activeSearchQuery.toLowerCase();
            const titleMatch = item.title.toLowerCase().includes(q);
            const minMatch = item.ministry.toLowerCase().includes(q);
            const bulletsMatch = item.bullets ? item.bullets.some(b => b.toLowerCase().includes(q)) : false;
            if (!titleMatch && !minMatch && !bulletsMatch) return false;
          }

          return true;
        });
      }

      function updateLeadCard(item) {
        if (!item || !leadTitleLink) return;
        leadTitleLink.textContent = item.title;
        leadTitleLink.href = item.url;
        leadMinistry.textContent = item.ministry;
        leadReadtime.textContent = item.read_time;
        leadDate.textContent = item.date;
        leadCta.href = item.url;

        const leadImg = document.getElementById('lead-story-img');
        const leadImgLink = document.getElementById('lead-story-img-link');
        if (leadImg && item.img) {
          leadImg.src = item.img;
          leadImg.alt = item.title;
          if (item.is_photo) {
            leadImg.className = 'w-full h-full object-cover transition-all duration-300 group-hover:scale-105';
          } else {
            leadImg.className = 'w-16 h-16 sm:w-20 sm:h-20 object-contain p-1.5 transition-all duration-300 group-hover:scale-105';
          }
        }
        if (leadImgLink) {
          leadImgLink.href = item.url;
          leadImgLink.setAttribute('aria-label', `Read ${item.title}`);
        }

        if (leadBullets) {
          leadBullets.innerHTML = '';
          const takeBullets = (item.bullets && item.bullets.length > 0) ? item.bullets.slice(0, 2) : [];
          if (takeBullets.length > 0) {
            takeBullets.forEach(b => {
              const li = document.createElement('li');
              li.className = 'flex items-start gap-2';
              li.innerHTML = `<span class="text-pib-700 dark:text-blue-400 font-bold shrink-0 mt-0.5">●</span><span class="line-clamp-2">${b}</span>`;
              leadBullets.appendChild(li);
            });
          } else {
            const li = document.createElement('li');
            li.className = 'text-slate-600 dark:text-zinc-400 line-clamp-2';
            li.textContent = item.title;
            leadBullets.appendChild(li);
          }
        }

        if (leadShare) {
          leadShare.setAttribute('data-url', item.url);
          leadShare.setAttribute('data-title', item.title);
        }
      }

      function renderReleases() {
        const filtered = getFilteredReleases();
        const totalItems = filtered.length;
        const totalPages = Math.max(1, Math.ceil(totalItems / pageSize));
        if (currentRelPage > totalPages) currentRelPage = totalPages;

        const startIndex = (currentRelPage - 1) * pageSize;
        const pageItems = filtered.slice(startIndex, startIndex + pageSize);

        // Update count text & pagination summary
        const displayStart = totalItems === 0 ? 0 : startIndex + 1;
        const displayEnd = Math.min(startIndex + pageSize, totalItems);
        const summaryText = `Showing releases ${displayStart}–${displayEnd} of ${totalItems} (Page ${currentRelPage} of ${totalPages})`;
        if (paginationSummary) paginationSummary.textContent = summaryText;
        if (countBadge) countBadge.textContent = `Showing releases ${displayStart}–${displayEnd} of ${totalItems}`;

        // Pagination buttons state
        if (btnPrevPage) btnPrevPage.disabled = currentRelPage <= 1;
        if (btnNextPage) btnNextPage.disabled = currentRelPage >= totalPages;

        // Render Pagination Pills
        if (pillsContainer) {
          pillsContainer.innerHTML = '';
          for (let p = 1; p <= totalPages; p++) {
            const pill = document.createElement('button');
            const isActive = p === currentRelPage;
            pill.className = isActive 
              ? 'page-num-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-pib-700 text-white shadow-xs'
              : 'page-num-btn px-3 py-1.5 rounded-xl text-xs font-bold text-slate-600 dark:text-zinc-300 hover:bg-slate-200 dark:hover:bg-zinc-800 transition-colors';
            pill.textContent = p;
            pill.setAttribute('aria-label', `Go to page ${p}`);
            pill.addEventListener('click', () => {
              currentRelPage = p;
              renderReleases();
            });
            pillsContainer.appendChild(pill);
          }
        }

        if (pageItems.length === 0) {
          if (riverContainer) riverContainer.innerHTML = '<div class="p-8 text-center text-slate-500">No releases found matching your search.</div>';
          if (gridContainer) gridContainer.innerHTML = '<div class="p-8 text-center text-slate-500 col-span-3">No releases found matching your search.</div>';
          return;
        }

        // 1. UPDATE LEAD STORY (First item of current page)
        const leadItem = pageItems[0];
        updateLeadCard(leadItem);

        // 2. RENDER RIVER STORIES (Remaining companion items on page)
        if (riverContainer) {
          riverContainer.innerHTML = '';
          const riverItems = pageItems.slice(1);

          if (riverItems.length === 0) {
            const div = document.createElement('div');
            div.className = 'p-6 text-center text-xs text-slate-400 italic bg-white dark:bg-zinc-900 rounded-2xl border border-slate-200 dark:border-zinc-800';
            div.textContent = 'Showing featured dispatch for this page.';
            riverContainer.appendChild(div);
          } else {
            riverItems.forEach((item) => {
              const card = document.createElement('div');
              card.className = 'river-item p-2.5 sm:p-3 bg-white dark:bg-zinc-900 rounded-xl border border-slate-200 dark:border-zinc-800/90 shadow-2xs hover:shadow-sm hover:border-pib-700/60 dark:hover:border-blue-500/60 transition-all cursor-pointer flex gap-3 items-center group';
              
              const bulletSnippet = (item.bullets && item.bullets[0]) ? item.bullets[0] : '';

              card.innerHTML = `
                <div class="relative w-14 h-14 sm:w-16 sm:h-16 rounded-lg overflow-hidden shrink-0 bg-slate-50 dark:bg-zinc-800 border border-slate-200/70 dark:border-zinc-700/70 flex items-center justify-center">
                  <img src="${item.img}" alt="${item.title}" class="${item.is_photo ? 'w-full h-full object-cover group-hover:scale-105 transition-transform duration-300' : 'w-10 h-10 sm:w-12 sm:h-12 object-contain p-1 group-hover:scale-105 transition-transform duration-300'}" loading="lazy">
                </div>
                <div class="flex-1 min-w-0 flex flex-col justify-between">
                  <div class="flex items-center justify-between gap-2 mb-0.5">
                    <span class="text-[11px] font-bold text-pib-700 dark:text-blue-400 truncate max-w-[200px] sm:max-w-[320px]">
                      ${item.ministry}
                    </span>
                    <span class="text-[10px] text-slate-400 font-mono shrink-0">
                      ${item.date}
                    </span>
                  </div>
                  <h4 class="text-xs sm:text-[13px] font-bold text-slate-900 dark:text-zinc-100 group-hover:text-pib-700 dark:group-hover:text-blue-400 transition-colors line-clamp-1 leading-snug">
                    <a href="${item.url}" class="focus:outline-none">${item.title}</a>
                  </h4>
                  ${bulletSnippet ? `<p class="text-[11px] text-slate-500 dark:text-zinc-400 line-clamp-1 mt-0.5 leading-normal hidden sm:block">${bulletSnippet}</p>` : ''}
                  <div class="mt-1 flex items-center justify-between text-[10px] text-slate-400">
                    <span class="font-mono">${item.read_time}</span>
                    <div class="flex items-center gap-2">
                      <button class="btn-share-mini hover:text-slate-700 dark:hover:text-zinc-200 transition-colors p-0.5" title="Share release" data-url="${item.url}" data-title="${item.title}">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
                      </button>
                      <a href="${item.url}" class="font-bold text-pib-700 dark:text-blue-400 hover:underline">Read →</a>
                    </div>
                  </div>
                </div>
              `;

              // Click river card to preview on Left Lead Card
              card.addEventListener('click', (e) => {
                if (e.target.tagName === 'A' || e.target.closest('a') || e.target.closest('button')) return;
                updateLeadCard(item);
                document.querySelectorAll('.river-item').forEach(el => el.classList.remove('ring-2', 'ring-pib-700', 'bg-pib-50/40', 'dark:bg-zinc-800/60'));
                card.classList.add('ring-2', 'ring-pib-700', 'bg-pib-50/40', 'dark:bg-zinc-800/60');
              });

              riverContainer.appendChild(card);
            });
          }
        }

        // 3. RENDER GRID VIEW (All items on page)
        if (gridContainer) {
          gridContainer.innerHTML = '';
          pageItems.forEach(item => {
            const card = document.createElement('article');
            card.className = 'bg-white dark:bg-zinc-900 rounded-2xl border border-slate-200 dark:border-zinc-800 shadow-xs hover:shadow-md transition-all flex flex-col justify-between overflow-hidden group';
            
            let bulletsHtml = '';
            if (item.bullets && item.bullets.length > 0) {
              bulletsHtml = '<ul class="mt-3 space-y-1.5 text-xs text-slate-600 dark:text-zinc-400">';
              item.bullets.forEach(b => {
                bulletsHtml += `<li class="flex items-start gap-1.5"><span class="text-pib-700 dark:text-blue-400 font-bold shrink-0 mt-0.5">●</span><span class="line-clamp-2">${b}</span></li>`;
              });
              bulletsHtml += '</ul>';
            }

            const imgHtml = `
              <div class="relative w-full aspect-video bg-slate-50 dark:bg-zinc-800/80 border-b border-slate-100 dark:border-zinc-800 flex items-center justify-center overflow-hidden">
                <img src="${item.img}" alt="${item.title}" class="${item.is_photo ? 'w-full h-full object-cover group-hover:scale-105 transition-transform duration-500' : 'w-20 h-20 sm:w-24 sm:h-24 object-contain p-2 group-hover:scale-105 transition-transform duration-300'}" loading="lazy">
                ${item.top ? '<span class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-500 text-white shadow-xs">Top Story</span>' : ''}
              </div>
            `;

            card.innerHTML = `
              ${imgHtml}
              <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between">
                <div>
                  <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold text-pib-700 dark:text-blue-400 truncate max-w-[220px]">${item.ministry}</span>
                  </div>
                  <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-snug line-clamp-2 sm:line-clamp-3 hover:text-pib-700 transition-colors">
                    <a href="${item.url}">${item.title}</a>
                  </h3>
                  ${bulletsHtml}
                </div>
                <div class="mt-4 pt-3 border-t border-slate-100 dark:border-zinc-800 flex items-center justify-between text-xs text-slate-500">
                  <div class="flex items-center gap-2 font-mono text-[11px]">
                    <time>${item.date}</time>
                    <span>·</span>
                    <span>${item.read_time}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <button class="btn-share-mini hover:text-slate-700 dark:hover:text-zinc-200 transition-colors p-1" title="Share release" data-url="${item.url}" data-title="${item.title}">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
                    </button>
                    <a href="${item.url}" class="font-bold text-pib-700 dark:text-blue-400 hover:underline">Read →</a>
                  </div>
                </div>
              </div>
            `;
            gridContainer.appendChild(card);
          });
        }
      }

      // Prev / Next button listeners
      if (btnPrevPage) {
        btnPrevPage.addEventListener('click', () => {
          if (currentRelPage > 1) {
            currentRelPage--;
            renderReleases();
          }
        });
      }
      if (btnNextPage) {
        btnNextPage.addEventListener('click', () => {
          const filtered = getFilteredReleases();
          const totalPages = Math.ceil(filtered.length / pageSize);
          if (currentRelPage < totalPages) {
            currentRelPage++;
            renderReleases();
          }
        });
      }

      // Tab listeners
      const tabLatest = document.getElementById('tab-rel-latest');
      const tabTop = document.getElementById('tab-rel-top');
      const tabMostread = document.getElementById('tab-rel-mostread');

      function setRelCategoryTab(tab, btn) {
        activeCategoryTab = tab;
        currentRelPage = 1;
        [tabLatest, tabTop, tabMostread].forEach(b => {
          if (b) {
            b.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-pib-700 dark:hover:text-white";
            b.setAttribute('aria-selected', 'false');
          }
        });
        if (btn) {
          btn.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white dark:bg-zinc-700 text-pib-700 dark:text-white shadow-xs";
          btn.setAttribute('aria-selected', 'true');
        }
        renderReleases();
      }

      if (tabLatest) tabLatest.addEventListener('click', () => setRelCategoryTab('latest', tabLatest));
      if (tabTop) tabTop.addEventListener('click', () => setRelCategoryTab('top', tabTop));
      if (tabMostread) tabMostread.addEventListener('click', () => setRelCategoryTab('mostread', tabMostread));

      // Keyword search listener
      const relSearchInput = document.getElementById('releases-keyword-filter');
      if (relSearchInput) {
        relSearchInput.addEventListener('input', (e) => {
          activeSearchQuery = e.target.value.trim();
          currentRelPage = 1;
          renderReleases();
        });
      }

      // Ministry filter chips listeners
      const chipButtons = document.querySelectorAll('.chip-filter');
      chipButtons.forEach(chip => {
        chip.addEventListener('click', () => {
          chipButtons.forEach(c => {
            c.className = "chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-all whitespace-nowrap";
          });
          chip.className = "chip-filter px-2.5 py-1 rounded-lg text-[11px] font-bold bg-pib-700 text-white transition-all whitespace-nowrap";
          activeMinistryFilter = chip.getAttribute('data-ministry');
          currentRelPage = 1;
          renderReleases();
        });
      });

      // View Switcher listeners: Lead & River vs Full Grid
      const btnViewSplit = document.getElementById('btn-view-split');
      const btnViewGrid = document.getElementById('btn-view-grid');

      if (btnViewSplit && btnViewGrid && splitView && gridContainer) {
        btnViewSplit.addEventListener('click', () => {
          activeViewMode = 'split';
          btnViewSplit.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-white dark:bg-zinc-700 text-pib-700 dark:text-white shadow-xs flex items-center gap-1.5 transition-all";
          btnViewSplit.setAttribute('aria-pressed', 'true');
          btnViewGrid.className = "px-3 py-1.5 rounded-lg text-xs font-bold text-slate-600 dark:text-zinc-400 hover:text-pib-700 dark:hover:text-white flex items-center gap-1.5 transition-all";
          btnViewGrid.setAttribute('aria-pressed', 'false');
          splitView.classList.remove('hidden');
          gridContainer.classList.add('hidden');
          gridContainer.classList.remove('grid');
        });

        btnViewGrid.addEventListener('click', () => {
          activeViewMode = 'grid';
          btnViewGrid.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-white dark:bg-zinc-700 text-pib-700 dark:text-white shadow-xs flex items-center gap-1.5 transition-all";
          btnViewGrid.setAttribute('aria-pressed', 'true');
          btnViewSplit.className = "px-3 py-1.5 rounded-lg text-xs font-bold text-slate-600 dark:text-zinc-400 hover:text-pib-700 dark:hover:text-white flex items-center gap-1.5 transition-all";
          btnViewSplit.setAttribute('aria-pressed', 'false');
          splitView.classList.add('hidden');
          gridContainer.classList.remove('hidden');
          gridContainer.classList.add('grid');
        });
      }

      // Initial render of releases
      renderReleases();

      // Global Search forwarding
      const globalSearch = document.getElementById('global-search');
      if (globalSearch && relSearchInput) {
        globalSearch.addEventListener('input', (e) => {
          relSearchInput.value = e.target.value;
          activeSearchQuery = e.target.value.trim();
          currentRelPage = 1;
          renderReleases();
          const relSec = document.getElementById('releases');
          if (relSec) relSec.scrollIntoView({ behavior: 'smooth' });
        });
      }

      // 6. MEDIA DESK TABS
      const tabAdv = document.getElementById('tab-media-advisory');
      const tabServ = document.getElementById('tab-media-services');
      const pnlAdv = document.getElementById('panel-media-advisory');
      const pnlServ = document.getElementById('panel-media-services');

      if (tabAdv && tabServ) {
        tabAdv.addEventListener('click', () => {
          tabAdv.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white dark:bg-zinc-700 text-slate-900 dark:text-white shadow-xs";
          tabAdv.setAttribute('aria-selected', 'true');
          tabServ.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-slate-900";
          tabServ.setAttribute('aria-selected', 'false');
          if (pnlAdv) pnlAdv.classList.remove('hidden');
          if (pnlServ) pnlServ.classList.add('hidden');
        });

        tabServ.addEventListener('click', () => {
          tabServ.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white dark:bg-zinc-700 text-slate-900 dark:text-white shadow-xs";
          tabServ.setAttribute('aria-selected', 'true');
          tabAdv.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all text-slate-600 dark:text-zinc-300 hover:text-slate-900";
          tabAdv.setAttribute('aria-selected', 'false');
          if (pnlAdv) pnlAdv.classList.add('hidden');
          if (pnlServ) {
            pnlServ.classList.remove('hidden');
            pnlServ.classList.add('grid');
          }
        });
      }

      // 7. EXPLAINERS FILTERING & HORIZONTAL SCROLL
      const expContainer = document.getElementById('explainers-carousel');
      const btnExpLeft = document.getElementById('btn-scroll-explainers-left');
      const btnExpRight = document.getElementById('btn-scroll-explainers-right');
      const explainerTabs = document.querySelectorAll('.explainer-filter-btn');

      if (explainerTabs.length > 0) {
        explainerTabs.forEach(tab => {
          tab.addEventListener('click', () => {
            explainerTabs.forEach(t => {
              t.className = "explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:bg-slate-200 transition-colors whitespace-nowrap";
            });
            tab.className = "explainer-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-emerald-700 text-white shadow-xs whitespace-nowrap";

            const filter = tab.getAttribute('data-filter');
            const cards = document.querySelectorAll('.explainer-card');
            cards.forEach(c => {
              const badge = c.getAttribute('data-badge');
              if (filter === 'all') {
                c.classList.remove('hidden');
              } else if (filter === 'Factsheets' && badge === 'Factsheet') {
                c.classList.remove('hidden');
              } else if (filter === 'Backgrounders' && badge === 'Backgrounder') {
                c.classList.remove('hidden');
              } else {
                c.classList.add('hidden');
              }
            });
          });
        });
      }

      if (btnExpLeft && expContainer) {
        btnExpLeft.addEventListener('click', () => {
          expContainer.scrollBy({ left: -300, behavior: 'smooth' });
        });
      }
      if (btnExpRight && expContainer) {
        btnExpRight.addEventListener('click', () => {
          expContainer.scrollBy({ left: 300, behavior: 'smooth' });
        });
      }

      // 8. VIDEO PLAYLIST SWITCHER
      const mainVidThumb = document.getElementById('main-video-thumbnail');
      const mainVidTitle = document.getElementById('main-video-title');
      const mainVidDate = document.getElementById('main-video-date');
      const mainVidTag = document.getElementById('main-video-tag');
      const mainVidDuration = document.getElementById('main-video-duration');
      const playlistItems = document.querySelectorAll('.video-playlist-item');

      playlistItems.forEach(item => {
        item.addEventListener('click', () => {
          const img = item.getAttribute('data-img');
          const title = item.getAttribute('data-title');
          const date = item.getAttribute('data-date');
          const tag = item.getAttribute('data-tag');
          const duration = item.getAttribute('data-duration');

          if (mainVidThumb) mainVidThumb.src = img;
          if (mainVidTitle) mainVidTitle.textContent = title;
          if (mainVidDate) mainVidDate.textContent = date;
          if (mainVidTag) mainVidTag.textContent = tag;
          if (mainVidDuration) mainVidDuration.textContent = duration;

          playlistItems.forEach(it => {
            it.className = "video-playlist-item w-full text-left p-2 rounded-xl border border-transparent hover:bg-slate-50 dark:hover:bg-zinc-800/60 flex items-center gap-3 transition-all group";
          });
          item.className = "video-playlist-item w-full text-left p-2 rounded-xl border border-red-600 bg-red-50/50 dark:bg-zinc-800 flex items-center gap-3 transition-all group";
        });
      });

      // 9. PHOTO LIGHTBOX MODAL
      const photoModal = document.getElementById('photo-modal');
      const modalImg = document.getElementById('modal-img');
      const modalCaption = document.getElementById('modal-caption');
      const modalLoc = document.getElementById('modal-loc');
      const modalDate = document.getElementById('modal-date');
      const modalClose = document.getElementById('btn-modal-close');
      const featPhotoWrap = document.getElementById('featured-photo-wrapper');
      const thumbBtns = document.querySelectorAll('.photo-thumb-btn');

      function openModal(photo) {
        if (!photoModal) return;
        modalImg.src = photo.img;
        modalCaption.textContent = photo.caption;
        modalLoc.textContent = photo.location;
        modalDate.textContent = photo.date;
        photoModal.classList.remove('hidden');
        photoModal.classList.add('flex');
        document.body.style.overflow = 'hidden';
      }

      function closeModal() {
        if (!photoModal) return;
        photoModal.classList.add('hidden');
        photoModal.classList.remove('flex');
        document.body.style.overflow = '';
      }

      if (featPhotoWrap) {
        featPhotoWrap.addEventListener('click', () => openModal(photos[0]));
      }
      thumbBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const idx = parseInt(btn.getAttribute('data-photo-index'), 10);
          if (photos[idx]) openModal(photos[idx]);
        });
      });
      if (modalClose) modalClose.addEventListener('click', closeModal);
      if (photoModal) {
        photoModal.addEventListener('click', (e) => {
          if (e.target === photoModal) closeModal();
        });
      }
      window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && photoModal && !photoModal.classList.contains('hidden')) closeModal();
      });

      // 10. COOKIE BANNER
      const cookieBanner = document.getElementById('cookie-banner');
      const cookieAccept = document.getElementById('btn-cookie-accept');
      const cookieDismiss = document.getElementById('btn-cookie-dismiss');
      const footerCookieBtn = document.getElementById('footer-cookie-btn');

      if (cookieAccept) {
        cookieAccept.addEventListener('click', () => {
          if (cookieBanner) cookieBanner.classList.add('hidden');
        });
      }
      if (cookieDismiss) {
        cookieDismiss.addEventListener('click', () => {
          if (cookieBanner) cookieBanner.classList.add('hidden');
        });
      }
      if (footerCookieBtn) {
        footerCookieBtn.addEventListener('click', (e) => {
          e.preventDefault();
          if (cookieBanner) cookieBanner.classList.remove('hidden');
        });
      }

      // 11. SOCIAL SHARE BUTTONS
      document.addEventListener('click', async (e) => {
        const btn = e.target.closest('.btn-share-mini, #lead-story-share');
        if (!btn) return;
        e.stopPropagation();
        const title = btn.getAttribute('data-title');
        const url = btn.getAttribute('data-url');
        if (navigator.share) {
          try {
            await navigator.share({ title, url: window.location.origin + url });
          } catch (err) {}
        } else {
          navigator.clipboard.writeText(window.location.origin + url);
          btn.classList.add('text-emerald-600');
          setTimeout(() => btn.classList.remove('text-emerald-600'), 1500);
        }
      });

      // 12. BLOGS HORIZONTAL SCROLL
      const blogContainer = document.getElementById('blogs-carousel');
      const btnBlogLeft = document.getElementById('btn-scroll-blogs-left');
      const btnBlogRight = document.getElementById('btn-scroll-blogs-right');

      if (btnBlogLeft && blogContainer) {
        btnBlogLeft.addEventListener('click', () => {
          blogContainer.scrollBy({ left: -320, behavior: 'smooth' });
        });
      }
      if (btnBlogRight && blogContainer) {
        btnBlogRight.addEventListener('click', () => {
          blogContainer.scrollBy({ left: 320, behavior: 'smooth' });
        });
      }

      // 13. LIVE CLOCK (IST)
      function updateLiveClock() {
        const clockEl = document.getElementById('live-clock');
        if (!clockEl) return;
        const now = new Date();
        const options = {
          timeZone: 'Asia/Kolkata',
          weekday: 'short',
          day: '2-digit',
          month: 'long',
          year: 'numeric',
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit',
          hour12: true
        };
        const formatted = new Intl.DateTimeFormat('en-IN', options).format(now);
        clockEl.textContent = formatted.replace(',', '') + ' IST';
      }
      setInterval(updateLiveClock, 1000);
      updateLiveClock();

    })();
  </script>
</body>
</html>
"""

    parts.append(js_content)
    return "".join(parts)

if __name__ == "__main__":
    html_output = build_current_page()
    with open("current-page.htm", "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"current-page.htm successfully regenerated. File size: {len(html_output)} bytes")

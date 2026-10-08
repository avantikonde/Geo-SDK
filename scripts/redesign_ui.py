#!/usr/bin/env python3
"""
redesign_ui.py
Enhances the FaultGraph UI with high-craft, elegant animations:
1. Ambient aurora depth mesh with slow breathing oscillation
2. Harmonic zero-G floating physics on 3D nodes (alive organic network)
3. Glowing energy pulses and interactive light waves along edges
4. Cinematic camera fly-to interpolation with spring damping
5. Spotlight cursor tracking and border shimmer on incident cards
6. Staggered cascade entrance for catalog cards
7. Animated sliding segmented control for layout switcher
8. Smooth count-up counter animation for header metrics
9. Spring-scale modal entrances and slide-in sidepanel inspector
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract DEFAULT_INCIDENTS verbatim
default_incidents_match = re.search(r'(const DEFAULT_INCIDENTS = \[[\s\S]*?\n    \];)', orig)
if not default_incidents_match:
    raise ValueError("Could not find DEFAULT_INCIDENTS in index.html")
default_incidents_code = default_incidents_match.group(1)

# Extract fetchGeoKnowledgeGraph verbatim
fetch_geo_match = re.search(r'(async function fetchGeoKnowledgeGraph\(\) \{[\s\S]*?\n    \})', orig)
if not fetch_geo_match:
    raise ValueError("Could not find fetchGeoKnowledgeGraph in index.html")
fetch_geo_code = fetch_geo_match.group(1)

new_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FaultGraph — AI Agent Incident &amp; Vulnerability Knowledge Graph</title>
  <link rel="icon" type="image/png" href="logo.png">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,400;0,500;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; }}
    html, body {{
      background: #08090d;
      color: #F4F4F5;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
      overflow-y: auto;
    }}
    .mono {{ font-family: 'DM Mono', monospace; }}

    /* Custom Sleek Scrollbars */
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: rgba(8, 9, 13, 0.6); }}
    ::-webkit-scrollbar-thumb {{ background: rgba(255, 255, 255, 0.15); border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: rgba(255, 255, 255, 0.28); }}

    /* Ambient Aurora Glow Animation */
    @keyframes ambientShift {{
      0%, 100% {{
        transform: scale(1) translate(0, 0);
        opacity: 0.65;
      }}
      50% {{
        transform: scale(1.08) translate(-1.5%, 1%);
        opacity: 0.9;
      }}
    }}
    .ambient-aurora {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      background: 
        radial-gradient(ellipse 65% 50% at 20% 20%, rgba(56, 189, 248, 0.08) 0%, transparent 60%),
        radial-gradient(ellipse 60% 45% at 85% 75%, rgba(244, 63, 94, 0.06) 0%, transparent 60%),
        radial-gradient(ellipse 50% 50% at 50% 45%, rgba(16, 185, 129, 0.04) 0%, transparent 65%);
      animation: ambientShift 16s ease-in-out infinite;
      z-index: 1;
    }}

    /* Live Beacon Ring Animation */
    @keyframes pulseRing {{
      0% {{
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6);
      }}
      70% {{
        box-shadow: 0 0 0 6px rgba(16, 185, 129, 0);
      }}
      100% {{
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
      }}
    }}
    .live-beacon {{
      animation: pulseRing 2.4s infinite cubic-bezier(0.4, 0, 0.6, 1);
    }}

    /* Glass Surfaces */
    .glass-panel {{
      background: rgba(14, 16, 23, 0.78);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
      transition: border-color 0.25s ease, background-color 0.25s ease;
    }}

    /* Card Spotlight & Border Shimmer Effect (Linear / Vercel style) */
    .glass-card {{
      position: relative;
      background: rgba(15, 17, 24, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.07);
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), 
                  border-color 0.28s cubic-bezier(0.16, 1, 0.3, 1), 
                  background-color 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                  box-shadow 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: hidden;
    }}
    .glass-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(255, 255, 255, 0.04) 50%,
        transparent 100%
      );
      transition: left 0.65s ease;
      pointer-events: none;
    }}
    .glass-card:hover::before {{
      left: 100%;
    }}
    .glass-card:hover {{
      background: rgba(22, 25, 36, 0.9);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-4px) scale(1.008);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7), 0 0 25px -5px rgba(56, 189, 248, 0.12);
    }}

    /* Staggered Card Entrance */
    @keyframes cardEntrance {{
      from {{
        opacity: 0;
        transform: translateY(18px) scale(0.97);
      }}
      to {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}
    .card-animate {{
      animation: cardEntrance 0.45s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}

    /* Minimalist Segmented Controls */
    .ctrl-btn {{
      background: transparent;
      border: 1px solid transparent;
      color: #94A3B8;
      font-size: 11px;
      font-weight: 500;
      padding: 5px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: color 0.18s ease, transform 0.12s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      position: relative;
      user-select: none;
    }}
    .ctrl-btn:hover {{
      color: #FFFFFF;
    }}
    .ctrl-btn:active {{
      transform: scale(0.96);
    }}
    .ctrl-btn.active {{
      color: #FFFFFF;
    }}

    /* Pill sliding background on segmented container */
    #layout-pill-bg {{
      position: absolute;
      top: 4px;
      bottom: 4px;
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
      z-index: 0;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 7px;
      border-radius: 6px;
      font-weight: 500;
      font-size: 10px;
    }}

    /* Canvas cursor */
    #graph-canvas {{
      cursor: grab;
      display: block;
      width: 100%;
      height: 100%;
      position: relative;
      z-index: 2;
    }}
    #graph-canvas:active {{
      cursor: grabbing;
    }}

    /* Floating Tooltip */
    #graph-tooltip {{
      position: absolute;
      display: none;
      background: rgba(10, 12, 18, 0.94);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 12px;
      padding: 10px 14px;
      max-width: 300px;
      pointer-events: none;
      z-index: 40;
      box-shadow: 0 16px 36px rgba(0,0,0,0.65), 0 0 15px rgba(56, 189, 248, 0.1);
      backdrop-filter: blur(16px);
      transition: opacity 0.15s ease-out, transform 0.15s ease-out;
      transform: translate3d(0, 0, 0);
    }}

    /* Modal Scale-In Animation */
    @keyframes modalEntrance {{
      0% {{
        opacity: 0;
        transform: scale(0.95) translateY(10px);
      }}
      100% {{
        opacity: 1;
        transform: scale(1) translateY(0);
      }}
    }}
    .modal-animated {{
      animation: modalEntrance 0.26s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    /* Sidepanel slide & fade transitions */
    .sp-fade-item {{
      animation: cardEntrance 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-zinc-700 selection:text-white relative">

  <!-- TOAST NOTIFICATION -->
  <div id="toast-banner" class="fixed top-5 left-1/2 -translate-x-1/2 z-[110] pointer-events-none hidden transition-all duration-300">
    <div class="px-4 py-2 rounded-full bg-zinc-900/95 border border-white/15 text-xs shadow-2xl flex items-center space-x-2 backdrop-blur-xl text-zinc-100">
      <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
      <span id="toast-text" class="font-medium">Incident registered</span>
    </div>
  </div>

  <!-- TOP APP HEADER -->
  <header class="border-b border-white/[0.08] bg-zinc-950/85 backdrop-blur-xl sticky top-0 z-40 px-6 py-2.5 flex items-center justify-between">
    <div class="flex items-center space-x-3">
      <div class="cursor-pointer flex items-center space-x-2.5 group" onclick="scrollToSection('section-graph')" title="FaultGraph 3D Canvas">
        <div class="relative">
          <img src="logo.png" alt="FaultGraph Logo" class="h-8 w-8 rounded-lg object-contain bg-zinc-900 border border-white/10 p-0.5 shadow-sm group-hover:border-sky-400/50 transition-colors">
          <span class="absolute -bottom-0.5 -right-0.5 w-2 h-2 rounded-full bg-emerald-400 live-beacon"></span>
        </div>
        <span class="font-semibold text-sm tracking-tight text-zinc-100 group-hover:text-white transition-colors">FaultGraph</span>
        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-zinc-800/80 text-zinc-400 border border-white/5">GRC-20</span>
      </div>
    </div>

    <!-- Center Navigation Tabs -->
    <nav class="hidden md:flex items-center space-x-1 p-1 rounded-xl bg-zinc-900/60 border border-white/5 text-xs text-zinc-400">
      <button onclick="scrollToSection('section-graph')" id="nav-btn-graph" class="px-3 py-1.5 rounded-lg text-white font-medium bg-white/10 transition hover:text-white">3D Graph</button>
      <button onclick="scrollToSection('section-catalog')" id="nav-btn-catalog" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition">Incident Catalog</button>
      <button onclick="scrollToSection('section-triples')" id="nav-btn-triples" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition">Triples Matrix</button>
    </nav>

    <!-- Right: Search, Stats, Geo Link, New Incident -->
    <div class="flex items-center space-x-2 text-xs">
      <!-- Search Input Container -->
      <div class="relative flex items-center" id="search-nav-container">
        <svg class="w-3.5 h-3.5 text-zinc-400 absolute left-3 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input id="search-input" type="text" oninput="handleGlobalSearch()" onfocus="handleGlobalSearch()" onkeydown="handleSearchKey(event)" placeholder="Search incidents, flaws, models..." class="w-36 sm:w-60 bg-zinc-900/80 border border-white/10 rounded-lg pl-8 pr-7 py-1.5 text-xs text-zinc-200 placeholder-zinc-500 focus:outline-none focus:border-zinc-400 focus:ring-1 focus:ring-zinc-400/30 transition">
        <button id="search-clear-btn" onclick="clearGlobalSearch()" class="hidden absolute right-2 text-zinc-400 hover:text-white text-xs font-bold px-1 transition" title="Clear search">✕</button>

        <!-- Category Dropdown -->
        <select id="search-category" onchange="handleGlobalSearch()" class="hidden">
          <option value="all">All Fields</option>
          <option value="Incident">Incidents</option>
          <option value="Agent">Agents</option>
          <option value="FailureMode">Failure Modes</option>
          <option value="Mitigation">Mitigations</option>
          <option value="FinancialLoss">Financial Losses</option>
        </select>

        <!-- Autocomplete Dropdown -->
        <div id="search-autocomplete-dropdown" class="hidden absolute top-full right-0 mt-2 w-80 sm:w-96 max-w-[calc(100vw-2rem)] max-h-96 overflow-y-auto bg-zinc-950/95 backdrop-blur-2xl border border-white/10 rounded-xl shadow-2xl p-2 z-[60] text-xs">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- Quick Metrics Pill (Animated Counter) -->
      <div class="hidden lg:flex items-center space-x-2 px-2.5 py-1.5 rounded-lg bg-zinc-900/80 border border-white/5 text-[11px] font-mono text-zinc-400 shadow-inner">
        <span class="text-zinc-100 font-semibold" id="stat-incidents">0</span>
        <span>incidents</span>
        <span class="text-zinc-600">·</span>
        <span class="text-amber-400/90 font-semibold" id="stat-loss">$0M</span>
        <span class="hidden" id="stat-agents">0</span>
        <span class="hidden" id="stat-mitigations">0</span>
      </div>

      <!-- Geo Link Badge -->
      <a href="https://www.geobrowser.io/space/fb47f7907b4cc91be446bbf9fb51ccad" target="_blank" rel="noopener" id="geo-source-badge" class="px-2.5 py-1.5 rounded-lg bg-zinc-900/80 hover:bg-zinc-800 border border-white/10 text-zinc-300 text-[11px] flex items-center space-x-1.5 transition active:scale-95" title="Connected to Geo Knowledge Graph Space fb47f7907b4cc91be446bbf9fb51ccad">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 live-beacon"></span>
        <span class="font-mono text-[10px]">Geo Testnet ↗</span>
      </a>

      <!-- New Incident Button -->
      <button onclick="openModal()" class="px-3 py-1.5 rounded-lg bg-zinc-100 hover:bg-white text-zinc-950 font-medium text-xs flex items-center space-x-1.5 transition active:scale-95 shadow-sm hover:shadow-md">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M12 4v16m8-8H4"/></svg>
        <span>New Incident</span>
      </button>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- SECTION 1: 3D INTERACTIVE KNOWLEDGE GRAPH VIEWPORT                        -->
  <!-- ========================================================================= -->
  <section id="section-graph" class="relative w-full h-[78vh] min-h-[580px] bg-[#08090d] border-b border-white/[0.08] flex flex-col md:flex-row overflow-hidden">

    <!-- Ambient Aurora Depth Layer -->
    <div class="ambient-aurora"></div>

    <!-- 3D Canvas Container -->
    <div id="canvas-container" class="flex-1 relative overflow-hidden select-none z-10">
      <canvas id="graph-canvas"></canvas>

      <!-- Active Filter Pill on Canvas -->
      <div id="graph-search-status" class="hidden absolute top-4 right-4 z-20 glass-panel px-3 py-1.5 rounded-xl text-xs flex items-center space-x-2 border border-white/10 shadow-lg">
        <span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>
        <span id="graph-search-status-text" class="text-zinc-200 font-medium"></span>
        <button onclick="clearGlobalSearch()" class="text-zinc-400 hover:text-rose-400 font-bold ml-1 transition" title="Clear filter">✕</button>
      </div>

      <!-- Top-Left Floating Controls Dock -->
      <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-20">
        <!-- Layout Switcher Segmented Control with Sliding Indicator Pill -->
        <div class="glass-panel p-1 rounded-xl flex items-center relative" id="layout-segmented-container">
          <!-- Animated sliding pill backdrop -->
          <div id="layout-pill-bg"></div>

          <button class="ctrl-btn active" id="btn-layout-cluster" onclick="setLayout('cluster')">
            <span>System Cluster</span>
          </button>
          <button class="ctrl-btn" id="btn-layout-causal" onclick="setLayout('causal')">
            <span>Causal Pipeline</span>
          </button>
          <button class="ctrl-btn" id="btn-layout-impact" onclick="setLayout('impact')">
            <span>Severity Altitude</span>
          </button>
        </div>

        <!-- Camera Controls -->
        <div class="glass-panel p-1 rounded-xl flex items-center space-x-1">
          <button class="ctrl-btn active" id="btn-toggle-rotate" onclick="toggleAutoRotate()">
            <span id="rotate-text">Auto-Spin</span>
          </button>
          <button class="ctrl-btn" id="btn-reset-cam" onclick="resetCamera()">
            <span>Reset View</span>
          </button>
        </div>
      </div>

      <!-- Bottom-Left Floating Relations Filter -->
      <div class="absolute bottom-4 left-4 z-20 glass-panel p-1.5 rounded-xl flex flex-wrap items-center gap-1 text-xs">
        <span class="text-[10px] uppercase font-mono font-medium text-zinc-500 px-1.5">Relations:</span>
        <button class="ctrl-btn active text-[11px] px-2 py-1 rounded-md" id="btn-edge-all" onclick="toggleEdgeFilter('all')">All</button>
        <button class="ctrl-btn active text-[11px] px-2 py-1 rounded-md" id="btn-edge-agent" onclick="toggleEdgeFilter('involves_agent')">
          <span class="w-1.5 h-1.5 rounded-full bg-sky-400 inline-block mr-0.5"></span>Agents
        </button>
        <button class="ctrl-btn active text-[11px] px-2 py-1 rounded-md" id="btn-edge-failure" onclick="toggleEdgeFilter('exhibits')">
          <span class="w-1.5 h-1.5 rounded-full bg-amber-400 inline-block mr-0.5"></span>Failures
        </button>
        <button class="ctrl-btn active text-[11px] px-2 py-1 rounded-md" id="btn-edge-mitigation" onclick="toggleEdgeFilter('mitigated_by')">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 inline-block mr-0.5"></span>Mitigations
        </button>
        <button class="ctrl-btn active text-[11px] px-2 py-1 rounded-md" id="btn-edge-loss" onclick="toggleEdgeFilter('resulted_in')">
          <span class="w-1.5 h-1.5 rounded-full bg-yellow-400 inline-block mr-0.5"></span>Losses
        </button>
      </div>

      <!-- Zoom Controls (Right Middle) -->
      <div class="absolute right-4 top-1/2 -translate-y-1/2 flex flex-col space-y-1.5 z-20 glass-panel p-1 rounded-xl">
        <button onclick="zoomIn()" class="w-7 h-7 flex items-center justify-center text-zinc-400 hover:text-white rounded-lg text-sm font-medium transition active:scale-90" title="Zoom In">+</button>
        <button onclick="zoomOut()" class="w-7 h-7 flex items-center justify-center text-zinc-400 hover:text-white rounded-lg text-sm font-medium transition active:scale-90" title="Zoom Out">−</button>
      </div>

      <!-- Floating Tooltip HUD -->
      <div id="graph-tooltip">
        <div id="tt-type" class="text-[10px] uppercase font-mono font-semibold tracking-wider text-sky-400 mb-0.5">Entity</div>
        <div id="tt-name" class="font-semibold text-xs text-white leading-snug mb-1">Entity Title</div>
        <div id="tt-meta" class="text-[11px] text-zinc-400 mb-2 leading-relaxed">Metadata description</div>
        <div id="tt-extra" class="pt-1.5 border-t border-white/[0.08] text-[10px] text-zinc-400 flex items-center justify-between">
          <span id="tt-conns" class="mono text-sky-300">0 connections</span>
          <span class="text-zinc-500">Click to fly in</span>
        </div>
      </div>
    </div>

    <!-- Slide-Out Deep Semantic Sidepanel -->
    <aside id="sidepanel" class="w-full md:w-96 border-t md:border-t-0 md:border-l border-white/[0.08] bg-zinc-950/90 flex flex-col justify-between shadow-2xl z-20 backdrop-blur-xl shrink-0 h-full">

      <!-- Sidepanel Fixed Header -->
      <div class="p-4 border-b border-white/[0.08] flex items-center justify-between shrink-0">
        <span class="text-xs uppercase tracking-wider font-semibold text-zinc-400 flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-sky-400 live-beacon"></span>
          <span>Knowledge Inspector</span>
        </span>
        <span id="sidepanel-type-badge" class="badge bg-zinc-800 text-zinc-300">Overview</span>
      </div>

      <!-- Sidepanel Scrollable Container -->
      <div id="sidepanel-scroll-container" class="flex-1 overflow-y-auto p-5 space-y-4 min-h-0">

        <!-- Empty Placeholder -->
        <div id="sidepanel-empty" class="text-center py-16 text-zinc-500 text-xs">
          <div class="w-12 h-12 rounded-xl bg-zinc-900 border border-white/5 flex items-center justify-center mx-auto mb-3 text-zinc-400 shadow-inner">
            <svg class="w-5 h-5 text-zinc-500 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/></svg>
          </div>
          <p class="font-medium text-zinc-300 mb-1">Select Any 3D Entity</p>
          <p class="text-zinc-500 leading-relaxed max-w-xs mx-auto">Click any node to view its verified post-mortem, parameters, and connected system relations.</p>
        </div>

        <!-- Populated Content Area -->
        <div id="sidepanel-content" class="hidden space-y-4">
          <div class="sp-fade-item">
            <div id="sp-category" class="text-[10px] uppercase font-mono font-semibold tracking-wider text-sky-400 mb-1">Incident</div>
            <h3 id="sp-title" class="font-semibold text-sm text-white leading-snug">Incident Name</h3>
            <p id="sp-desc" class="text-xs text-zinc-300 mt-2 leading-relaxed bg-zinc-900/60 p-3 rounded-xl border border-white/5">Description goes here.</p>
          </div>

          <!-- Verified Post-Mortem Quick Actions -->
          <div id="sp-actions" class="space-y-2 sp-fade-item">
            <button id="sp-read-report-btn" onclick="openPostMortemModalForCurrentNode()" class="w-full py-2 px-3 rounded-lg bg-zinc-100 hover:bg-white text-zinc-950 text-xs font-medium flex items-center justify-center space-x-2 transition active:scale-95 shadow-sm">
              <span>Read Full Post-Mortem →</span>
            </button>
            <a id="sp-link" href="#" target="_blank" rel="noopener" class="w-full py-2 px-3 rounded-lg bg-zinc-900 hover:bg-zinc-800 border border-white/10 text-zinc-300 text-xs font-medium flex items-center justify-center space-x-1.5 transition">
              <span id="sp-link-text">Official Source ↗</span>
            </a>
          </div>

          <!-- Attributes & Parameters -->
          <div class="space-y-2 pt-2 border-t border-white/[0.08] sp-fade-item">
            <h4 class="text-[11px] font-semibold text-zinc-400 uppercase tracking-wider flex items-center justify-between">
              <span>Attributes</span>
              <span class="text-[10px] text-zinc-500 font-mono">Parameters</span>
            </h4>
            <div id="sp-properties" class="space-y-1.5 text-xs">
              <!-- Injected via JS -->
            </div>
          </div>

          <!-- Connected Triples -->
          <div class="space-y-2 pt-2 border-t border-white/[0.08] sp-fade-item">
            <div class="flex items-center justify-between">
              <h4 class="text-[11px] font-semibold text-zinc-400 uppercase tracking-wider">Connected Triples</h4>
              <span class="text-[10px] text-zinc-500 font-mono">GRC-20 Relations</span>
            </div>
            <div id="sp-relations" class="space-y-1.5 text-xs">
              <!-- Injected via JS -->
            </div>
          </div>
        </div>

      </div>

    </aside>

  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 2: INCIDENT CATALOG & VERIFIED POST-MORTEM REPORTS               -->
  <!-- ========================================================================= -->
  <section id="section-catalog" class="py-12 px-6 sm:px-10 bg-[#08090d] border-b border-white/[0.08] relative">
    <div class="max-w-7xl mx-auto space-y-6">

      <!-- Section Header -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 pb-5 border-b border-white/[0.08]">
        <div>
          <h2 class="text-xl font-semibold text-white tracking-tight">Incident Catalog &amp; Post-Mortems</h2>
          <p class="text-xs text-zinc-400 mt-1">
            Verified dossiers of autonomous agent failures, court rulings, regulatory SEC filings, and engineering mitigations.
          </p>
        </div>

        <div class="flex items-center space-x-3 w-full md:w-auto">
          <input type="text" id="catalog-search" oninput="handleCatalogSearch()" placeholder="Filter incidents, models, flaws..." class="w-full md:w-72 bg-zinc-900/80 border border-white/10 rounded-lg px-3.5 py-2 text-xs text-zinc-200 placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
        </div>
      </div>

      <!-- Cards Grid with Staggered Animations -->
      <div id="catalog-cards-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <!-- Injected via JavaScript -->
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 3: SYSTEM TRIPLES SCHEMA MATRIX                                   -->
  <!-- ========================================================================= -->
  <section id="section-triples" class="py-12 px-6 sm:px-10 bg-[#06070a] border-b border-white/[0.08]">
    <div class="max-w-7xl mx-auto space-y-6">

      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-5 border-b border-white/[0.08]">
        <div>
          <h2 class="text-xl font-semibold text-white tracking-tight">Knowledge Graph Triples Matrix</h2>
          <p class="text-xs text-zinc-400 mt-1">Verifiable semantic relationships structured as Subject &rarr; Predicate &rarr; Object</p>
        </div>
        <button onclick="scrollToSection('section-graph')" class="px-3 py-1.5 rounded-lg bg-zinc-900 hover:bg-zinc-800 text-zinc-300 border border-white/10 text-xs font-medium transition active:scale-95">
          View in 3D &uarr;
        </button>
      </div>

      <div class="bg-zinc-900/40 border border-white/[0.08] rounded-xl overflow-hidden shadow-xl backdrop-blur-xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-zinc-900/80 border-b border-white/[0.08] text-zinc-400 font-medium uppercase font-mono text-[10px]">
              <tr>
                <th class="p-3.5 pl-5">Subject (Entity)</th>
                <th class="p-3.5">Predicate (Relation)</th>
                <th class="p-3.5">Object (Target Entity)</th>
                <th class="p-3.5 pr-5 text-right">Inspect Action</th>
              </tr>
            </thead>
            <tbody id="triples-table-body" class="divide-y divide-white/[0.05] text-zinc-300">
              <!-- Injected via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FULL POST-MORTEM REPORT MODAL                                            -->
  <!-- ========================================================================= -->
  <div id="postmortem-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] hidden flex items-center justify-center p-4">
    <div class="bg-zinc-950 border border-white/10 rounded-2xl max-w-2xl w-full max-h-[88vh] flex flex-col shadow-2xl relative overflow-hidden modal-animated">

      <!-- Modal Header -->
      <div class="p-5 border-b border-white/[0.08] flex items-start justify-between gap-4 shrink-0 bg-zinc-900/40">
        <div>
          <div class="flex items-center space-x-2 mb-1.5">
            <span id="pm-severity-badge" class="badge bg-rose-500/10 text-rose-300 border border-rose-500/20">Critical</span>
            <span id="pm-source-badge" class="badge bg-zinc-800 text-zinc-300">Verified Source</span>
            <span id="pm-date" class="mono text-[11px] text-zinc-500">2026-04-18</span>
          </div>
          <h2 id="pm-title" class="text-base font-semibold text-white tracking-tight leading-snug">Incident Post-Mortem Report</h2>
        </div>
        <button onclick="closePostMortemModal()" class="w-8 h-8 rounded-lg bg-zinc-900 text-zinc-400 hover:text-white flex items-center justify-center text-lg font-medium transition active:scale-95 shrink-0">&times;</button>
      </div>

      <!-- Modal Scrollable Content -->
      <div id="pm-body" class="p-6 overflow-y-auto space-y-5 text-xs leading-relaxed text-zinc-300">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-white/[0.08] flex items-center justify-between shrink-0 bg-zinc-900/60">
        <span class="text-zinc-500 text-xs font-mono">FaultGraph Audit Dossier</span>
        <div class="flex items-center space-x-2.5">
          <a id="pm-external-link" href="#" target="_blank" rel="noopener" class="px-3.5 py-1.5 rounded-lg bg-zinc-100 hover:bg-white text-zinc-950 font-medium text-xs shadow-sm transition flex items-center space-x-1.5 active:scale-95">
            <span>Open External Source ↗</span>
          </a>
          <button onclick="closePostMortemModal()" class="px-3.5 py-1.5 rounded-lg bg-zinc-900 hover:bg-zinc-800 text-zinc-300 font-medium text-xs transition border border-white/5 active:scale-95">
            Close
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- ADD INCIDENT MODAL                                                        -->
  <!-- ========================================================================= -->
  <div id="add-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] hidden flex items-center justify-center p-4">
    <div class="bg-zinc-950 border border-white/10 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative space-y-4 modal-animated">
      <div class="flex items-center justify-between pb-3 border-b border-white/[0.08]">
        <div>
          <h3 class="text-sm font-semibold text-white tracking-tight">Add New Incident to 3D Graph</h3>
          <p class="text-[11px] text-zinc-400">Attaches new semantic triples to the knowledge graph</p>
        </div>
        <button onclick="closeModal()" class="w-7 h-7 rounded-lg bg-zinc-900 text-zinc-400 hover:text-white flex items-center justify-center text-base font-medium transition active:scale-95">&times;</button>
      </div>

      <form id="incident-form" onsubmit="handleFormSubmit(event)" class="space-y-3.5 text-xs">
        <div>
          <label class="block text-zinc-300 font-medium mb-1">Incident Title *</label>
          <input type="text" id="form-name" required placeholder="e.g. Flash Arbitrage LLM Order Splitting Failure" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Incident Date *</label>
            <input type="date" id="form-date" required class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2 text-white focus:outline-none focus:border-zinc-400 transition">
          </div>
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Severity *</label>
            <select id="form-severity" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2 text-white focus:outline-none focus:border-zinc-400 transition">
              <option value="Critical">Critical (Destroyed State / High Loss)</option>
              <option value="High">High (Privilege Breach / Slippage Loop)</option>
              <option value="Medium">Medium (Hallucination / Bounded Loss)</option>
              <option value="Low">Low (Minor Prompt Incoherence)</option>
            </select>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Agent Name *</label>
            <input type="text" id="form-agent" required placeholder="e.g. DeFi-Arbitrageur-v2" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
          </div>
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Agent Architecture</label>
            <input type="text" id="form-arch" placeholder="e.g. LangGraph Router" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
          </div>
        </div>

        <div>
          <label class="block text-zinc-300 font-medium mb-1">Failure Mode (Root Cause) *</label>
          <input type="text" id="form-failure" required placeholder="e.g. Recursive Slippage Feedback Loop" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
        </div>

        <div>
          <label class="block text-zinc-300 font-medium mb-1">Mitigation Strategy *</label>
          <input type="text" id="form-mitigation" required placeholder="e.g. Dynamic Drawdown Circuit Breaker" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Financial Loss ($ USD)</label>
            <input type="number" id="form-loss" placeholder="e.g. 1200000" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
          </div>
          <div>
            <label class="block text-zinc-300 font-medium mb-1">Source / Post-Mortem URL</label>
            <input type="url" id="form-link" placeholder="https://example.com/postmortem" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-2.5 text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition">
          </div>
        </div>

        <div class="flex items-center justify-end space-x-2 pt-3 border-t border-white/[0.08]">
          <button type="button" onclick="closeModal()" class="px-3.5 py-2 rounded-lg bg-zinc-900 hover:bg-zinc-800 text-zinc-300 font-medium transition active:scale-95">Cancel</button>
          <button type="submit" class="px-4 py-2 rounded-lg bg-zinc-100 hover:bg-white text-zinc-950 font-medium shadow-sm transition active:scale-95">Add Triples to Graph</button>
        </div>
      </form>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- APPLICATION SCRIPT & ENGINE                                               -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // SMOOTH SCROLLING NAVIGATION
    // -------------------------------------------------------------------------
    function scrollToSection(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    // Safe silent sound no-ops
    function sfxClick() {{}}
    function sfxNodeSelect() {{}}
    function sfxLayout() {{}}
    function sfxModal() {{}}
    function sfxAlert() {{}}
    function sfxThreatLaser() {{}}
    function sfxImpactShockwave() {{}}
    function sfxDefenseShield() {{}}
    function playTone() {{}}

    // -------------------------------------------------------------------------
    // GLOBAL SEARCH & AUTOCOMPLETE ENGINE
    // -------------------------------------------------------------------------
    function escapeHtml(str) {{
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    function highlightQuery(text, query) {{
      if (!query || !text) return escapeHtml(text || '');
      const regex = new RegExp(`(${{query.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&')}})`, 'gi');
      return escapeHtml(text).replace(regex, '<span class="text-sky-300 font-semibold bg-sky-950/80 px-1 py-0.5 rounded">$1</span>');
    }}

    function handleGlobalSearch() {{
      const searchInput = document.getElementById('search-input');
      const catalogSearch = document.getElementById('catalog-search');
      const categorySelect = document.getElementById('search-category');
      const clearBtn = document.getElementById('search-clear-btn');
      const dropdown = document.getElementById('search-autocomplete-dropdown');
      const statusPill = document.getElementById('graph-search-status');
      const statusText = document.getElementById('graph-search-status-text');

      const query = (searchInput?.value || '').trim();
      const lowerQuery = query.toLowerCase();
      const searchCat = categorySelect?.value || 'all';

      if (clearBtn) {{
        clearBtn.classList.toggle('hidden', query.length === 0);
      }}

      if (catalogSearch && catalogSearch.value !== query) {{
        catalogSearch.value = query;
      }}

      // Collect matching nodes
      const matches = [];
      nodes.forEach(n => {{
        const matchesCat = (searchCat === 'all' || n.type === searchCat);
        let matchesQuery = true;
        if (lowerQuery) {{
          matchesQuery = n.name.toLowerCase().includes(lowerQuery) ||
                         (n.description && n.description.toLowerCase().includes(lowerQuery)) ||
                         (n.architecture && n.architecture.toLowerCase().includes(lowerQuery)) ||
                         (n.strategy && n.strategy.toLowerCase().includes(lowerQuery)) ||
                         (n.incidentRef && n.incidentRef.name.toLowerCase().includes(lowerQuery));
        }}
        if (matchesCat && matchesQuery) {{
          matches.push(n);
        }}
      }});

      // Update on-canvas filter status pill
      if (statusPill && statusText) {{
        if (query || searchCat !== 'all') {{
          const catLabel = categorySelect ? categorySelect.options[categorySelect.selectedIndex].text : searchCat;
          const queryPart = query ? `"${{query}}"` : '';
          const filterDesc = query && searchCat !== 'all' ? `${{queryPart}} in ${{catLabel}}` : query ? queryPart : catLabel;
          statusText.innerText = `Filtered: ${{filterDesc}} (${{matches.length}} found)`;
          statusPill.classList.remove('hidden');
        }} else {{
          statusPill.classList.add('hidden');
        }}
      }}

      // Populate interactive Autocomplete Dropdown
      if (dropdown) {{
        if (query.length > 0) {{
          dropdown.classList.remove('hidden');
          if (matches.length === 0) {{
            dropdown.innerHTML = `
              <div class="p-4 text-center text-zinc-400">
                <span class="block text-zinc-500 mb-1 font-mono text-[11px]">No results</span>
                No graph entities found matching "<span class="text-white">${{escapeHtml(query)}}</span>"
              </div>
            `;
          }} else {{
            let html = `
              <div class="px-3 py-1.5 text-[10px] uppercase font-mono font-semibold text-zinc-400 border-b border-white/[0.08] flex justify-between items-center bg-zinc-900/50 rounded-t-lg">
                <span>Matching Entities (${{matches.length}})</span>
                <span class="text-zinc-500 lowercase font-normal">click to fly in 3D</span>
              </div>
              <div class="divide-y divide-white/[0.05] max-h-72 overflow-y-auto">
            `;
            const sortedMatches = [...matches].sort((a, b) => {{
              const order = {{ Incident: 0, Agent: 1, FailureMode: 2, Mitigation: 3, FinancialLoss: 4 }};
              return (order[a.type] || 5) - (order[b.type] || 5);
            }}).slice(0, 10);

            sortedMatches.forEach(node => {{
              const typeColor = node.color || '#38BDF8';
              const parentInc = node.incidentRef ? node.incidentRef.name : '';
              html += `
                <div onclick="selectSearchResult('${{node.id}}')" class="p-2.5 rounded-lg hover:bg-zinc-800/60 cursor-pointer transition flex items-start space-x-2.5 group">
                  <span class="w-2 h-2 rounded-full shrink-0 mt-1" style="background:${{typeColor}}"></span>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between gap-1">
                      <span class="font-medium text-zinc-200 group-hover:text-white transition truncate text-xs">${{highlightQuery(node.name, query)}}</span>
                      <span class="text-[9px] px-1.5 py-0.5 rounded font-mono uppercase bg-zinc-800 text-zinc-400 shrink-0">${{node.type}}</span>
                    </div>
                    ${{node.description ? `<p class="text-[11px] text-zinc-400 truncate mt-0.5">${{escapeHtml(node.description)}}</p>` : ''}}
                    ${{parentInc && node.type !== 'Incident' ? `<p class="text-[10px] text-zinc-500 truncate mt-0.5">↳ In incident: ${{escapeHtml(parentInc)}}</p>` : ''}}
                  </div>
                </div>
              `;
            }});
            html += `</div>`;
            dropdown.innerHTML = html;
          }}
        }} else {{
          dropdown.classList.add('hidden');
        }}
      }}

      draw();
      renderIncidentCatalog();
      renderTriplesTable();
    }}

    function selectSearchResult(nodeId) {{
      const node = nodeMap[nodeId];
      if (!node) return;

      const searchInput = document.getElementById('search-input');
      if (searchInput) searchInput.value = node.name;
      const clearBtn = document.getElementById('search-clear-btn');
      if (clearBtn) clearBtn.classList.remove('hidden');

      const dropdown = document.getElementById('search-autocomplete-dropdown');
      if (dropdown) dropdown.classList.add('hidden');

      flyToNode(node);
    }}

    function clearGlobalSearch() {{
      const searchInput = document.getElementById('search-input');
      const catalogSearch = document.getElementById('catalog-search');
      const categorySelect = document.getElementById('search-category');
      const clearBtn = document.getElementById('search-clear-btn');
      const dropdown = document.getElementById('search-autocomplete-dropdown');
      const statusPill = document.getElementById('graph-search-status');

      if (searchInput) searchInput.value = '';
      if (catalogSearch) catalogSearch.value = '';
      if (categorySelect) categorySelect.value = 'all';
      if (clearBtn) clearBtn.classList.add('hidden');
      if (dropdown) dropdown.classList.add('hidden');
      if (statusPill) statusPill.classList.add('hidden');

      selectedNode = null;
      setHighlight(null);
      renderSidePanel(null);
      draw();
      renderIncidentCatalog();
      renderTriplesTable();
    }}

    function handleSearchKey(event) {{
      if (event.key === 'Enter') {{
        const query = (document.getElementById('search-input')?.value || '').trim().toLowerCase();
        const searchCat = document.getElementById('search-category')?.value || 'all';
        const match = nodes.find(n => {{
          const matchesCat = (searchCat === 'all' || n.type === searchCat);
          const matchesQuery = !query || n.name.toLowerCase().includes(query) || (n.description && n.description.toLowerCase().includes(query));
          return matchesCat && matchesQuery;
        }});
        if (match) {{
          selectSearchResult(match.id);
        }}
      }} else if (event.key === 'Escape') {{
        const dropdown = document.getElementById('search-autocomplete-dropdown');
        if (dropdown) dropdown.classList.add('hidden');
      }}
    }}

    function handleCatalogSearch() {{
      const catalogSearch = document.getElementById('catalog-search');
      const searchInput = document.getElementById('search-input');
      const query = (catalogSearch?.value || '').trim();

      if (searchInput && searchInput.value !== query) {{
        searchInput.value = query;
      }}

      handleGlobalSearch();
    }}

    document.addEventListener('click', (e) => {{
      const searchContainer = document.getElementById('search-nav-container');
      const dropdown = document.getElementById('search-autocomplete-dropdown');
      if (dropdown && searchContainer && !searchContainer.contains(e.target)) {{
        dropdown.classList.add('hidden');
      }}
    }});

    function showToast(msg) {{
      const banner = document.getElementById('toast-banner');
      document.getElementById('toast-text').innerText = msg;
      banner.classList.remove('hidden');
      setTimeout(() => banner.classList.add('hidden'), 2600);
    }}

    // -------------------------------------------------------------------------
    // VERIFIED REAL-WORLD INCIDENT DATA
    // -------------------------------------------------------------------------
    {default_incidents_code}

    // -------------------------------------------------------------------------
    // LOCAL STORAGE & GEO GRAPHQL PERSISTENCE
    // -------------------------------------------------------------------------
    const STORAGE_KEY = 'faultgraph_incidents_v16';
    let incidents = [];

    function loadIncidents() {{
      ['faultgraph_incidents_v1', 'faultgraph_incidents_v2', 'faultgraph_incidents_v3', 'faultgraph_incidents_v10', 'faultgraph_incidents_v14', 'faultgraph_incidents_v15'].forEach(k => {{
        try {{ localStorage.removeItem(k); }} catch(e) {{}}
      }});

      try {{
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {{
          const parsed = JSON.parse(stored);
          if (Array.isArray(parsed) && parsed.length > 0) {{
            incidents = parsed;
            const defaultMap = {{}};
            DEFAULT_INCIDENTS.forEach(d => {{ defaultMap[d.id] = d; }});
            incidents.forEach(inc => {{
              if (defaultMap[inc.id]) {{
                inc.sourceName = defaultMap[inc.id].sourceName;
                inc.sourceEvidenceLink = defaultMap[inc.id].sourceEvidenceLink;
                inc.secondaryLink = defaultMap[inc.id].secondaryLink;
              }}
            }});
            saveIncidents();
            fetchGeoKnowledgeGraph();
            return;
          }}
        }}
      }} catch (err) {{
        console.warn('Failed to parse incidents from localStorage, using defaults:', err);
      }}
      incidents = JSON.parse(JSON.stringify(DEFAULT_INCIDENTS));
      saveIncidents();
      fetchGeoKnowledgeGraph();
    }}

    function saveIncidents() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(incidents));
      }} catch (err) {{
        console.warn('Failed to save incidents to localStorage:', err);
      }}
    }}

    {fetch_geo_code}

    // -------------------------------------------------------------------------
    // 3D SPATIAL ENGINE & CAMERA INTERPOLATION
    // -------------------------------------------------------------------------
    const canvas = document.getElementById('graph-canvas');
    const ctx = canvas.getContext('2d');
    let W = canvas.width = window.innerWidth;
    let H = canvas.height = window.innerHeight;

    let nodes = [];
    let edges = [];
    let nodeMap = {{}};

    // Camera parameters
    let rotX = 0.35;
    let rotY = -0.55;
    let zoom = 52;
    let autoRotate = true;
    let dragging = false;
    let lastX = 0, lastY = 0;

    // Cinematic camera fly-to interpolation targets
    let targetRotX = 0.35;
    let targetRotY = -0.55;
    let targetZoom = 52;
    let cameraMoving = false;

    let hoveredNode = null;
    let hoveredEdge = null;
    let selectedNode = null;
    let hlNodes = new Set();
    let hlEdges = new Set();

    let edgeFilters = {{
      all: true,
      involves_agent: true,
      exhibits: true,
      mitigated_by: true,
      resulted_in: true
    }};

    let hiddenTypes = new Set();

    let currentLayout = 'cluster';
    let interpT = 1.0;
    let interpFrom = 'cluster';
    let interpTo = 'cluster';

    let flowParticles = [];
    const NUM_PARTICLES = 36;

    const TYPE_COLORS = {{
      Incident: '#F43F5E',     // Clean Rose
      Agent: '#38BDF8',        // Clean Sky Blue
      FailureMode: '#FB923C',  // Warm Amber / Orange
      Mitigation: '#10B981',   // Fresh Emerald
      FinancialLoss: '#EAB308' // Refined Gold
    }};

    function resizeCanvas() {{
      const container = document.getElementById('canvas-container');
      if (!container) return;
      W = canvas.width = container.clientWidth;
      H = canvas.height = container.clientHeight;
      draw();
    }}
    window.addEventListener('resize', resizeCanvas);

    function project(x, y, z) {{
      const cX = Math.cos(rotX), sX = Math.sin(rotX);
      const cY = Math.cos(rotY), sY = Math.sin(rotY);

      const y2 = y * cX - z * sX;
      const z2 = y * sX + z * cX;

      const x2 = x * cY + z2 * sY;
      const z3 = -x * sY + z2 * cY;

      const fov = 650;
      const d = fov / (fov + z3 * zoom * 0.32);

      return {{
        sx: W / 2 + x2 * zoom * d,
        sy: H / 2 + y2 * zoom * d,
        z: z3,
        d: d
      }};
    }}

    function getNodeCoord(node, layoutKey) {{
      if (layoutKey === 'cluster') return {{ x: node.cx, y: node.cy, z: node.cz }};
      if (layoutKey === 'causal') return {{ x: node.px, y: node.py, z: node.pz }};
      if (layoutKey === 'impact') return {{ x: node.ix, y: node.iy, z: node.iz }};
      return {{ x: node.cx, y: node.cy, z: node.cz }};
    }}

    function buildGraphData() {{
      nodes = [];
      edges = [];
      nodeMap = {{}};

      const count = incidents.length;

      incidents.forEach((inc, idx) => {{
        const clusterAngle = (idx / count) * Math.PI * 2;
        const clusterRadius = 8.6;
        const incX = Math.cos(clusterAngle) * clusterRadius;
        const incY = ((idx % 3) - 1) * 1.6;
        const incZ = Math.sin(clusterAngle) * clusterRadius;

        const satAngle = (i) => clusterAngle + (i * Math.PI / 2.2);
        const satR = 2.1;

        const rowY = (idx - count / 2) * 1.35;
        const rowZ = ((idx % 4) - 1.5) * 1.8;

        let sevY = 0;
        if (inc.severity === 'Critical') sevY = -5.5;
        else if (inc.severity === 'High') sevY = -2.0;
        else if (inc.severity === 'Medium') sevY = 1.8;
        else sevY = 4.5;
        const spreadAngle = (idx / count) * Math.PI * 2;
        const spreadR = 4.2;

        // 1. Incident Node
        const incNode = {{
          id: inc.id,
          name: inc.name,
          type: 'Incident',
          severity: inc.severity,
          date: inc.date,
          description: inc.description,
          sourceEvidenceLink: inc.sourceEvidenceLink,
          sourceName: inc.sourceName,
          incidentRef: inc,
          size: 15,
          color: TYPE_COLORS.Incident,
          cx: incX, cy: incY, cz: incZ,
          px: 0.5, py: rowY, pz: rowZ,
          ix: Math.cos(spreadAngle) * spreadR, iy: sevY, iz: Math.sin(spreadAngle) * spreadR,
          x: incX, y: incY, z: incZ,
          phase: idx * 0.72
        }};
        nodes.push(incNode);
        nodeMap[incNode.id] = incNode;

        // 2. Agent Node
        const agentNode = {{
          id: inc.agent.id,
          name: inc.agent.name,
          type: 'Agent',
          architecture: inc.agent.architecture,
          description: inc.agent.description,
          incidentRef: inc,
          size: 13,
          color: TYPE_COLORS.Agent,
          cx: incX + Math.cos(satAngle(0)) * satR, cy: incY - 1.2, cz: incZ + Math.sin(satAngle(0)) * satR,
          px: -6.5, py: rowY - 0.4, pz: rowZ + 0.6,
          ix: Math.cos(spreadAngle - 0.4) * (spreadR + 2.2), iy: sevY + 1.2, iz: Math.sin(spreadAngle - 0.4) * (spreadR + 2.2),
          x: incX, y: incY, z: incZ,
          phase: idx * 0.72 + 1.2
        }};
        nodes.push(agentNode);
        nodeMap[agentNode.id] = agentNode;

        // 3. Failure Mode Node
        const failureNode = {{
          id: inc.failureMode.id,
          name: inc.failureMode.name,
          type: 'FailureMode',
          description: inc.failureMode.description,
          incidentRef: inc,
          size: 12,
          color: TYPE_COLORS.FailureMode,
          cx: incX + Math.cos(satAngle(1)) * satR, cy: incY + 0.8, cz: incZ + Math.sin(satAngle(1)) * satR,
          px: -2.8, py: rowY + 0.5, pz: rowZ - 0.5,
          ix: Math.cos(spreadAngle + 0.3) * (spreadR + 1.6), iy: sevY - 1.0, iz: Math.sin(spreadAngle + 0.3) * (spreadR + 1.6),
          x: incX, y: incY, z: incZ,
          phase: idx * 0.72 + 2.4
        }};
        nodes.push(failureNode);
        nodeMap[failureNode.id] = failureNode;

        // 4. Mitigation Node
        const mitNode = {{
          id: inc.mitigation.id,
          name: inc.mitigation.name,
          type: 'Mitigation',
          strategy: inc.mitigation.strategy,
          description: inc.mitigation.description,
          incidentRef: inc,
          size: 13,
          color: TYPE_COLORS.Mitigation,
          cx: incX + Math.cos(satAngle(2)) * satR, cy: incY - 0.6, cz: incZ + Math.sin(satAngle(2)) * satR,
          px: 4.8, py: rowY - 0.9, pz: rowZ + 0.8,
          ix: Math.cos(spreadAngle + 0.8) * (spreadR - 1.2), iy: sevY + 2.2, iz: Math.sin(spreadAngle + 0.8) * (spreadR - 1.2),
          x: incX, y: incY, z: incZ,
          phase: idx * 0.72 + 3.6
        }};
        nodes.push(mitNode);
        nodeMap[mitNode.id] = mitNode;

        // 5. Financial Loss Node
        const lossNode = {{
          id: inc.financialLoss.id,
          name: `$${{(inc.financialLoss.amount).toLocaleString()}} Loss`,
          type: 'FinancialLoss',
          amount: inc.financialLoss.amount,
          currency: inc.financialLoss.currency,
          description: inc.financialLoss.description,
          incidentRef: inc,
          size: 12,
          color: TYPE_COLORS.FinancialLoss,
          cx: incX + Math.cos(satAngle(3)) * satR, cy: incY + 1.4, cz: incZ + Math.sin(satAngle(3)) * satR,
          px: 4.8, py: rowY + 0.9, pz: rowZ - 0.8,
          ix: Math.cos(spreadAngle - 0.7) * (spreadR + 2.0), iy: sevY - 2.0, iz: Math.sin(spreadAngle - 0.7) * (spreadR + 2.0),
          x: incX, y: incY, z: incZ,
          phase: idx * 0.72 + 4.8
        }};
        nodes.push(lossNode);
        nodeMap[lossNode.id] = lossNode;

        // Edges
        edges.push({{ source: inc.id, target: inc.agent.id, relation: 'involves_agent', label: 'involves_agent', color: '#38BDF8' }});
        edges.push({{ source: inc.id, target: inc.failureMode.id, relation: 'exhibits', label: 'exhibits', color: '#FB923C' }});
        edges.push({{ source: inc.failureMode.id, target: inc.mitigation.id, relation: 'mitigated_by', label: 'mitigated_by', color: '#10B981' }});
        edges.push({{ source: inc.id, target: inc.financialLoss.id, relation: 'resulted_in', label: 'resulted_in', color: '#EAB308' }});
      }});

      nodes.forEach(n => {{
        const c = getNodeCoord(n, currentLayout);
        n.x = c.x;
        n.y = c.y;
        n.z = c.z;
      }});

      flowParticles = [];
      for (let i = 0; i < NUM_PARTICLES; i++) {{
        flowParticles.push({{
          edgeIndex: Math.floor(Math.random() * edges.length),
          progress: Math.random(),
          speed: 0.004 + Math.random() * 0.007
        }});
      }}

      updateMetrics();
      renderIncidentCatalog();
      renderTriplesTable();
      updatePillIndicator();
      draw();
    }}

    // Animated Count-Up Numbers
    function animateCount(elemId, start, end, duration, prefix = '', suffix = '') {{
      const el = document.getElementById(elemId);
      if (!el) return;
      const startTime = performance.now();
      function update(now) {{
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3); // easeOutCubic
        const val = start + (end - start) * ease;
        el.innerText = `${{prefix}}${{val.toFixed(end % 1 === 0 ? 0 : 1)}}${{suffix}}`;
        if (progress < 1) requestAnimationFrame(update);
      }}
      requestAnimationFrame(update);
    }}

    function updateMetrics() {{
      const totalCount = incidents.length;
      const totalLoss = incidents.reduce((sum, item) => sum + (item.financialLoss.amount || 0), 0);
      const lossM = totalLoss / 1e6;

      animateCount('stat-incidents', 0, totalCount, 750);
      animateCount('stat-loss', 0, lossM, 900, '$', 'M');
    }}

    // Cinematic Fly-To Camera Transition
    function flyToNode(node) {{
      if (!node) return;
      scrollToSection('section-graph');

      const angleY = Math.atan2(node.x, node.z);
      targetRotY = -angleY;
      targetRotX = 0.22;
      targetZoom = 76;
      cameraMoving = true;

      selectedNode = node;
      setHighlight(node);
      renderSidePanel(node);
      draw();
    }}

    // -------------------------------------------------------------------------
    // 3D NODE RENDERING WITH HARMONIC BREATHING & AURA
    // -------------------------------------------------------------------------
    function drawNodeShape(sx, sy, r, node, isHovered, isSelected, isDimmed, isConnected, isSearchMatch = false) {{
      const col = node.color;
      const alpha = isDimmed ? '25' : isConnected ? 'FF' : 'E5';
      const time = Date.now() * 0.0025;

      ctx.save();

      // Fluid Breathing Aura for hovered or selected nodes
      if (isSelected || isHovered || (node.type === 'Incident' && !isDimmed)) {{
        const breathe = Math.sin(time * 2.5 + (node.phase || 0)) * 0.18 + 1.0;
        const auraR = r * (1.8 * breathe);
        const glowGrad = ctx.createRadialGradient(sx, sy, r * 0.2, sx, sy, auraR);
        glowGrad.addColorStop(0, col + (isHovered || isSelected ? '55' : '30'));
        glowGrad.addColorStop(0.5, col + (isHovered || isSelected ? '22' : '10'));
        glowGrad.addColorStop(1, col + '00');
        ctx.fillStyle = glowGrad;
        ctx.beginPath();
        ctx.arc(sx, sy, auraR, 0, Math.PI * 2);
        ctx.fill();
      }}

      // Animated target ring for search matches
      if (isSearchMatch) {{
        const matchPulse = r + 5 + Math.sin(time * 4) * 2.5;
        ctx.beginPath();
        ctx.arc(sx, sy, matchPulse, 0, Math.PI * 2);
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 1.8;
        ctx.stroke();
      }}

      ctx.beginPath();

      if (node.type === 'Incident') {{
        const currentR = isHovered ? r * 1.25 : r;
        ctx.arc(sx, sy, currentR, 0, Math.PI * 2);
        ctx.fillStyle = isDimmed ? col + '33' : col;
        ctx.fill();
        ctx.strokeStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = isHovered ? 2 : 1;
        ctx.stroke();

      }} else if (node.type === 'Agent') {{
        const size = isHovered ? r * 1.25 : r;
        ctx.moveTo(sx, sy - size * 1.2);
        ctx.lineTo(sx + size, sy);
        ctx.lineTo(sx, sy + size * 1.2);
        ctx.lineTo(sx - size, sy);
        ctx.closePath();
        ctx.fillStyle = col + alpha;
        ctx.fill();
        ctx.strokeStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = isHovered ? 2 : 1;
        ctx.stroke();

      }} else if (node.type === 'FailureMode') {{
        const size = isHovered ? r * 1.25 : r;
        for (let i = 0; i < 6; i++) {{
          const a = i * Math.PI / 3 - Math.PI / 6;
          const px = sx + size * Math.cos(a);
          const py = sy + size * Math.sin(a);
          if (i === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }}
        ctx.closePath();
        ctx.fillStyle = col + alpha;
        ctx.fill();
        ctx.strokeStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = isHovered ? 2 : 1;
        ctx.stroke();

      }} else if (node.type === 'Mitigation') {{
        const size = isHovered ? r * 1.25 : r;
        ctx.arc(sx, sy, size, 0, Math.PI * 2);
        ctx.fillStyle = col + alpha;
        ctx.fill();
        ctx.strokeStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = isHovered ? 2 : 1.2;
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(sx - size * 0.4, sy);
        ctx.lineTo(sx + size * 0.4, sy);
        ctx.moveTo(sx, sy - size * 0.4);
        ctx.lineTo(sx, sy + size * 0.4);
        ctx.strokeStyle = isDimmed ? '#10B98133' : '#FFFFFF';
        ctx.lineWidth = 1;
        ctx.stroke();

      }} else if (node.type === 'FinancialLoss') {{
        const s = (isHovered ? r * 1.2 : r * 0.95);
        ctx.rect(sx - s, sy - s, s * 2, s * 2);
        ctx.fillStyle = col + alpha;
        ctx.fill();
        ctx.strokeStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = isHovered ? 2 : 1;
        ctx.stroke();
      }}

      // Node Label
      if (!isDimmed && (isHovered || isSelected || isSearchMatch || node.type === 'Incident' || zoom > 65)) {{
        ctx.font = '500 11px "Plus Jakarta Sans", sans-serif';
        const labelText = node.name.length > 24 ? node.name.slice(0, 22) + '…' : node.name;
        const textW = ctx.measureText(labelText).width;
        ctx.fillStyle = 'rgba(10, 12, 18, 0.88)';
        ctx.fillRect(sx - textW / 2 - 4, sy + r + 4, textW + 8, 16);
        ctx.strokeStyle = isSearchMatch ? '#FFFFFF' : 'rgba(255, 255, 255, 0.12)';
        ctx.lineWidth = 0.5;
        ctx.strokeRect(sx - textW / 2 - 4, sy + r + 4, textW + 8, 16);

        ctx.fillStyle = (isHovered || isSelected || isSearchMatch ? '#FFFFFF' : '#A1A1AA');
        ctx.textAlign = 'center';
        ctx.fillText(labelText, sx, sy + r + 16);
        ctx.textAlign = 'left';
      }}

      ctx.restore();
    }}

    function draw() {{
      ctx.clearRect(0, 0, W, H);

      // Subtle precision coordinate grid
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.015)';
      ctx.lineWidth = 1;
      const gridSize = 70;
      for (let x = 0; x < W; x += gridSize) {{
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }}
      for (let y = 0; y < H; y += gridSize) {{
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }}

      const time = Date.now() * 0.0018;

      // Smooth Layout Morphing
      if (interpT < 1.0) {{
        interpT = Math.min(1.0, interpT + 0.045);
        const t = interpT < 0.5 ? 4 * interpT * interpT * interpT : 1 - Math.pow(-2 * interpT + 2, 3) / 2;
        nodes.forEach(n => {{
          const from = getNodeCoord(n, interpFrom);
          const to = getNodeCoord(n, interpTo);
          n.x = from.x + (to.x - from.x) * t;
          n.y = from.y + (to.y - from.y) * t;
          n.z = from.z + (to.z - from.z) * t;
        }});
      }}

      // Search matching & Category filtering
      const searchQuery = (document.getElementById('search-input')?.value || document.getElementById('catalog-search')?.value || '').trim().toLowerCase();
      const searchCat = document.getElementById('search-category')?.value || 'all';
      let matchedNodeIds = null;

      if (searchQuery || searchCat !== 'all') {{
        matchedNodeIds = new Set();
        nodes.forEach(n => {{
          const matchesCat = (searchCat === 'all' || n.type === searchCat);
          let matchesQuery = true;
          if (searchQuery) {{
            matchesQuery = n.name.toLowerCase().includes(searchQuery) ||
                           (n.description && n.description.toLowerCase().includes(searchQuery)) ||
                           (n.architecture && n.architecture.toLowerCase().includes(searchQuery)) ||
                           (n.strategy && n.strategy.toLowerCase().includes(searchQuery)) ||
                           (n.incidentRef && n.incidentRef.name.toLowerCase().includes(searchQuery));
          }}
          if (matchesCat && matchesQuery) {{
            matchedNodeIds.add(n.id);
            if (searchCat === 'all' && n.type === 'Incident' && n.incidentRef) {{
              if (n.incidentRef.agent?.id) matchedNodeIds.add(n.incidentRef.agent.id);
              if (n.incidentRef.failureMode?.id) matchedNodeIds.add(n.incidentRef.failureMode.id);
              if (n.incidentRef.mitigation?.id) matchedNodeIds.add(n.incidentRef.mitigation.id);
              if (n.incidentRef.financialLoss?.id) matchedNodeIds.add(n.incidentRef.financialLoss.id);
            }}
          }}
        }});
      }}

      const hasActiveHighlight = (hoveredNode !== null || hoveredEdge !== null || selectedNode !== null);

      // Project nodes with subtle zero-G harmonic oscillation
      const projectedNodes = nodes.map(n => {{
        const floatY = Math.sin(time + (n.phase || 0)) * 0.12;
        const floatX = Math.cos(time * 0.8 + (n.phase || 0)) * 0.08;
        return {{
          ...project(n.x + floatX, n.y + floatY, n.z),
          node: n
        }};
      }});

      projectedNodes.sort((a, b) => a.z - b.z);

      // Draw Edges
      edges.forEach((e) => {{
        const s = nodeMap[e.source];
        const t = nodeMap[e.target];
        if (!s || !t) return;
        if (hiddenTypes.has(s.type) || hiddenTypes.has(t.type)) return;
        if (!edgeFilters.all && !edgeFilters[e.relation]) return;

        const isHl = hlEdges.has(e);
        const isDimmed = (hasActiveHighlight && !isHl) || (matchedNodeIds && !matchedNodeIds.has(e.source) && !matchedNodeIds.has(e.target));

        const ps = project(s.x, s.y, s.z);
        const pt = project(t.x, t.y, t.z);

        ctx.beginPath();
        ctx.moveTo(ps.sx, ps.sy);
        ctx.lineTo(pt.sx, pt.sy);

        if (isHl) {{
          ctx.strokeStyle = '#FFFFFF';
          ctx.lineWidth = 2.0;
        }} else if (isDimmed) {{
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
          ctx.lineWidth = 0.5;
        }} else {{
          ctx.strokeStyle = (e.color || '#38BDF8') + '35';
          ctx.lineWidth = 0.9;
        }}
        ctx.stroke();

        // Interactive light wave pulse along highlighted edges
        if (isHl) {{
          const wavePhase = (time * 1.5) % 1.0;
          const wx = s.x + (t.x - s.x) * wavePhase;
          const wy = s.y + (t.y - s.y) * wavePhase;
          const wz = s.z + (t.z - s.z) * wavePhase;
          const pw = project(wx, wy, wz);
          if (pw.d > 0) {{
            ctx.beginPath();
            ctx.arc(pw.sx, pw.sy, Math.max(2.5, 4.5 * pw.d), 0, Math.PI * 2);
            ctx.fillStyle = '#FFFFFF';
            ctx.fill();
          }}
        }}
      }});

      // Flow Particles along edges with soft radiant glow
      if (!hoveredNode) {{
        flowParticles.forEach(p => {{
          const edge = edges[p.edgeIndex];
          if (!edge) return;
          const s = nodeMap[edge.source];
          const t = nodeMap[edge.target];
          if (!s || !t || hiddenTypes.has(s.type) || hiddenTypes.has(t.type)) return;

          p.progress += p.speed;
          if (p.progress > 1.0) p.progress = 0;

          const px = s.x + (t.x - s.x) * p.progress;
          const py = s.y + (t.y - s.y) * p.progress;
          const pz = s.z + (t.z - s.z) * p.progress;

          const pt = project(px, py, pz);
          if (pt.d > 0) {{
            ctx.beginPath();
            ctx.arc(pt.sx, pt.sy, Math.max(1.5, 2.8 * pt.d), 0, Math.PI * 2);
            ctx.fillStyle = edge.color || '#38BDF8';
            ctx.fill();
          }}
        }});
      }}

      // Draw Nodes
      projectedNodes.forEach(({{ sx, sy, d, node }}) => {{
        if (hiddenTypes.has(node.type)) return;

        const isHovered = hoveredNode && hoveredNode.id === node.id;
        const isSelected = selectedNode && selectedNode.id === node.id;
        const isConnected = hlNodes.has(node.id);
        const isSearchMatch = Boolean(matchedNodeIds && matchedNodeIds.has(node.id));
        const isSearchDim = matchedNodeIds && !isSearchMatch;
        const isDimmed = (hasActiveHighlight && !isConnected) || isSearchDim;

        const nodeRadius = Math.max(4, node.size * d * (zoom / 45));

        drawNodeShape(sx, sy, nodeRadius, node, isHovered, isSelected, isDimmed, isConnected, isSearchMatch);
      }});
    }}

    function animate() {{
      if (autoRotate && !dragging && !cameraMoving) {{
        rotY += 0.0016;
      }}

      // Smooth camera interpolation
      if (cameraMoving && !dragging) {{
        rotX += (targetRotX - rotX) * 0.08;
        rotY += (targetRotY - rotY) * 0.08;
        zoom += (targetZoom - zoom) * 0.08;
        if (Math.abs(targetRotX - rotX) < 0.001 && Math.abs(targetRotY - rotY) < 0.001 && Math.abs(targetZoom - zoom) < 0.1) {{
          rotX = targetRotX;
          rotY = targetRotY;
          zoom = targetZoom;
          cameraMoving = false;
        }}
      }}

      draw();
      requestAnimationFrame(animate);
    }}

    // -------------------------------------------------------------------------
    // HIT TESTING & HIGHLIGHTING
    // -------------------------------------------------------------------------
    function getNodeAt(mx, my) {{
      let found = null;
      let bestDist = 26;

      nodes.forEach(n => {{
        if (hiddenTypes.has(n.type)) return;
        const p = project(n.x, n.y, n.z);
        const dist = Math.hypot(p.sx - mx, p.sy - my);
        const hitRadius = Math.max(14, n.size * p.d * (zoom / 45) * 1.5);
        if (dist < hitRadius && dist < bestDist) {{
          bestDist = dist;
          found = {{ node: n, sx: p.sx, sy: p.sy }};
        }}
      }});
      return found;
    }}

    function setHighlight(node) {{
      hlNodes.clear();
      hlEdges.clear();

      if (node) {{
        hlNodes.add(node.id);
        edges.forEach(e => {{
          if (e.source === node.id || e.target === node.id) {{
            hlEdges.add(e);
            hlNodes.add(e.source);
            hlNodes.add(e.target);
          }}
        }});
      }}
    }}

    // -------------------------------------------------------------------------
    // CANVAS INTERACTION EVENTS
    // -------------------------------------------------------------------------
    canvas.addEventListener('mousedown', e => {{
      dragging = true;
      cameraMoving = false;
      lastX = e.clientX;
      lastY = e.clientY;
      autoRotate = false;
      const text = document.getElementById('rotate-text');
      if (text) text.innerText = 'Paused';
      const btn = document.getElementById('btn-toggle-rotate');
      if (btn) btn.classList.remove('active');
    }});

    window.addEventListener('mouseup', () => {{
      dragging = false;
    }});

    canvas.addEventListener('mousemove', e => {{
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      if (dragging) {{
        rotY += (e.clientX - lastX) * 0.008;
        rotX += (e.clientY - lastY) * 0.008;
        rotX = Math.max(-Math.PI / 2.2, Math.min(Math.PI / 2.2, rotX));
        lastX = e.clientX;
        lastY = e.clientY;
        draw();
        return;
      }}

      const hit = getNodeAt(mx, my);
      const tooltip = document.getElementById('graph-tooltip');

      if (hit) {{
        hoveredNode = hit.node;
        setHighlight(hit.node);

        const n = hit.node;
        document.getElementById('tt-type').innerText = n.type;
        document.getElementById('tt-type').style.color = n.color;
        document.getElementById('tt-name').innerText = n.name;
        document.getElementById('tt-meta').innerText = n.description || (n.architecture ? `Arch: ${{n.architecture}}` : 'Knowledge graph entity');

        const connectedEdges = edges.filter(e => e.source === n.id || e.target === n.id);
        document.getElementById('tt-conns').innerText = `${{connectedEdges.length}} connections`;

        tooltip.style.display = 'block';
        tooltip.style.left = Math.min(hit.sx + 16, W - 300) + 'px';
        tooltip.style.top = Math.max(hit.sy - 70, 16) + 'px';

        draw();
      }} else {{
        if (hoveredNode) {{
          hoveredNode = null;
          if (!selectedNode) setHighlight(null);
          else setHighlight(selectedNode);
          tooltip.style.display = 'none';
          draw();
        }}
      }}
    }});

    canvas.addEventListener('mouseleave', () => {{
      dragging = false;
      hoveredNode = null;
      if (!selectedNode) setHighlight(null);
      else setHighlight(selectedNode);
      document.getElementById('graph-tooltip').style.display = 'none';
      draw();
    }});

    canvas.addEventListener('click', e => {{
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const hit = getNodeAt(mx, my);

      if (hit) {{
        flyToNode(hit.node);
      }} else {{
        selectedNode = null;
        setHighlight(null);
        renderSidePanel(null);
        draw();
      }}
    }});

    canvas.addEventListener('wheel', e => {{
      e.preventDefault();
      cameraMoving = false;
      const delta = e.deltaY > 0 ? 0.94 : 1.06;
      zoom = Math.max(22, Math.min(180, zoom * delta));
      draw();
    }}, {{ passive: false }});

    // Touch support
    canvas.addEventListener('touchstart', e => {{
      if (e.touches.length === 1) {{
        dragging = true;
        cameraMoving = false;
        lastX = e.touches[0].clientX;
        lastY = e.touches[0].clientY;
        autoRotate = false;
      }}
    }});
    canvas.addEventListener('touchmove', e => {{
      if (dragging && e.touches.length === 1) {{
        rotY += (e.touches[0].clientX - lastX) * 0.008;
        rotX += (e.touches[0].clientY - lastY) * 0.008;
        lastX = e.touches[0].clientX;
        lastY = e.touches[0].clientY;
        draw();
      }}
    }});
    canvas.addEventListener('touchend', () => dragging = false);

    // -------------------------------------------------------------------------
    // LAYOUT SWITCHING & PILL SLIDER
    // -------------------------------------------------------------------------
    function updatePillIndicator() {{
      const activeBtn = document.querySelector('#layout-segmented-container .ctrl-btn.active');
      const pill = document.getElementById('layout-pill-bg');
      if (activeBtn && pill) {{
        pill.style.left = activeBtn.offsetLeft + 'px';
        pill.style.width = activeBtn.offsetWidth + 'px';
      }}
    }}
    window.addEventListener('resize', updatePillIndicator);

    function setLayout(layoutMode) {{
      if (currentLayout === layoutMode && interpT >= 1.0) return;

      interpFrom = currentLayout;
      currentLayout = layoutMode;
      interpTo = layoutMode;
      interpT = 0;

      document.querySelectorAll('#btn-layout-cluster, #btn-layout-causal, #btn-layout-impact').forEach(btn => btn.classList.remove('active'));
      document.getElementById(`btn-layout-${{layoutMode}}`)?.classList.add('active');

      updatePillIndicator();
      draw();
    }}

    function toggleAutoRotate() {{
      autoRotate = !autoRotate;
      const btn = document.getElementById('btn-toggle-rotate');
      if (btn) btn.classList.toggle('active', autoRotate);
      const text = document.getElementById('rotate-text');
      if (text) text.innerText = autoRotate ? 'Auto-Spin' : 'Paused';
    }}

    function resetCamera() {{
      cameraMoving = true;
      targetRotX = 0.35;
      targetRotY = -0.55;
      targetZoom = 52;
      selectedNode = null;
      setHighlight(null);
      renderSidePanel(null);
      draw();
    }}

    function zoomIn() {{
      cameraMoving = false;
      zoom = Math.min(180, zoom * 1.15);
      draw();
    }}

    function zoomOut() {{
      cameraMoving = false;
      zoom = Math.max(22, zoom * 0.86);
      draw();
    }}

    function toggleEdgeFilter(type) {{
      if (type === 'all') {{
        const next = !edgeFilters.all;
        edgeFilters.all = next;
        edgeFilters.involves_agent = next;
        edgeFilters.exhibits = next;
        edgeFilters.mitigated_by = next;
        edgeFilters.resulted_in = next;
      }} else {{
        edgeFilters[type] = !edgeFilters[type];
        edgeFilters.all = (edgeFilters.involves_agent && edgeFilters.exhibits && edgeFilters.mitigated_by && edgeFilters.resulted_in);
      }}

      document.getElementById('btn-edge-all').classList.toggle('active', edgeFilters.all);
      document.getElementById('btn-edge-agent').classList.toggle('active', edgeFilters.involves_agent);
      document.getElementById('btn-edge-failure').classList.toggle('active', edgeFilters.exhibits);
      document.getElementById('btn-edge-mitigation').classList.toggle('active', edgeFilters.mitigated_by);
      document.getElementById('btn-edge-loss').classList.toggle('active', edgeFilters.resulted_in);

      draw();
    }}

    // -------------------------------------------------------------------------
    // SIDEPANEL INSPECTOR
    // -------------------------------------------------------------------------
    function renderSidePanel(node) {{
      const emptyState = document.getElementById('sidepanel-empty');
      const contentState = document.getElementById('sidepanel-content');
      const badge = document.getElementById('sidepanel-type-badge');

      if (!node) {{
        emptyState.classList.remove('hidden');
        contentState.classList.add('hidden');
        badge.innerText = 'Overview';
        badge.className = 'badge bg-zinc-800 text-zinc-300';
        return;
      }}

      emptyState.classList.add('hidden');
      contentState.classList.remove('hidden');

      badge.innerText = node.type;
      badge.style.backgroundColor = node.color + '20';
      badge.style.color = node.color;
      badge.style.border = `1px solid ${{node.color}}40`;

      document.getElementById('sp-category').innerText = `Entity · ${{node.type}}`;
      document.getElementById('sp-category').style.color = node.color;
      document.getElementById('sp-title').innerText = node.name;
      document.getElementById('sp-desc').innerText = node.description || 'Verified entity registered in FaultGraph.';

      const inc = node.incidentRef;
      const readBtn = document.getElementById('sp-read-report-btn');
      const linkBtn = document.getElementById('sp-link');
      const linkText = document.getElementById('sp-link-text');

      if (inc) {{
        readBtn.style.display = 'flex';
        if (inc.isFromGeo || (inc.id && inc.id.length === 32)) {{
          linkBtn.href = `https://www.geobrowser.io/space/fb47f7907b4cc91be446bbf9fb51ccad/${{inc.id}}`;
          linkText.innerText = 'View on Geo Browser (GRC-20) ↗';
        }} else {{
          linkBtn.href = inc.sourceEvidenceLink;
          linkText.innerText = inc.sourceName ? `${{inc.sourceName}} ↗` : 'Official Source ↗';
        }}
        linkBtn.style.display = 'flex';
      }} else {{
        readBtn.style.display = 'none';
        linkBtn.style.display = 'none';
      }}

      // Attributes Box
      const propsContainer = document.getElementById('sp-properties');
      propsContainer.innerHTML = '';

      const makeProp = (label, val, highlight = false) => {{
        return `
          <div class="flex items-center justify-between p-2 rounded-lg bg-zinc-900/80 border border-white/5 transition hover:border-white/10">
            <span class="text-zinc-400 font-medium">${{label}}:</span>
            <span class="font-medium ${{highlight ? 'text-amber-400 font-mono' : 'text-zinc-200'}}">${{val}}</span>
          </div>
        `;
      }};

      propsContainer.innerHTML += makeProp('Entity ID', node.id);
      if (node.incidentRef?.isFromGeo || (node.id && node.id.length === 32)) {{
        propsContainer.innerHTML += `
          <div class="flex items-center justify-between p-2 rounded-lg bg-zinc-900/80 border border-white/10">
            <span class="text-sky-300 font-mono text-[11px] flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 live-beacon"></span>Geo Testnet Entity
            </span>
            <a href="https://www.geobrowser.io/space/fb47f7907b4cc91be446bbf9fb51ccad/${{node.id}}" target="_blank" rel="noopener" class="text-sky-400 hover:text-white font-mono text-[11px] underline">
              View on Geo ↗
            </a>
          </div>
        `;
      }}
      if (node.severity) propsContainer.innerHTML += makeProp('Severity', node.severity, true);
      if (node.date) propsContainer.innerHTML += makeProp('Incident Date', node.date);
      if (node.architecture) propsContainer.innerHTML += makeProp('Architecture', node.architecture);
      if (node.strategy) propsContainer.innerHTML += makeProp('Mitigation Strategy', node.strategy);
      if (node.amount) propsContainer.innerHTML += makeProp('Loss Amount', `$${{node.amount.toLocaleString()}} ${{node.currency || 'USD'}}`, true);

      // Connected Triples
      const relsContainer = document.getElementById('sp-relations');
      relsContainer.innerHTML = '';
      const connectedEdges = edges.filter(e => e.source === node.id || e.target === node.id);

      if (connectedEdges.length === 0) {{
        relsContainer.innerHTML = '<p class="text-zinc-500 italic">No direct connections.</p>';
      }} else {{
        connectedEdges.forEach(e => {{
          const isSource = e.source === node.id;
          const otherId = isSource ? e.target : e.source;
          const otherNode = nodeMap[otherId];
          const otherName = otherNode ? otherNode.name : otherId;

          relsContainer.innerHTML += `
            <div onclick="selectNodeById('${{otherId}}')" class="p-2 rounded-lg bg-zinc-900/80 hover:bg-zinc-800 border border-white/5 cursor-pointer transition flex items-center justify-between group active:scale-98">
              <span class="text-[11px] text-zinc-300 group-hover:text-white transition-colors">
                <span class="text-sky-400 font-mono">${{e.relation}}</span> &rarr; ${{otherName}}
              </span>
              <span class="text-[10px] text-zinc-500 group-hover:text-zinc-300 transition-colors">&rarr;</span>
            </div>
          `;
        }});
      }}
    }}

    function selectNodeById(id) {{
      const node = nodeMap[id];
      if (node) {{
        flyToNode(node);
      }}
    }}

    function openPostMortemModalForCurrentNode() {{
      if (selectedNode && selectedNode.incidentRef) {{
        openPostMortemModal(selectedNode.incidentRef.id);
      }}
    }}

    // -------------------------------------------------------------------------
    // INCIDENT CATALOG RENDERING WITH STAGGERED REVEALS
    // -------------------------------------------------------------------------
    function renderIncidentCatalog() {{
      const query = ((document.getElementById('search-input')?.value || document.getElementById('catalog-search')?.value) || '').trim().toLowerCase();
      const searchCat = document.getElementById('search-category')?.value || 'all';
      const container = document.getElementById('catalog-cards-container');
      if (!container) return;
      container.innerHTML = '';

      const filtered = incidents.filter(i => {{
        if (searchCat === 'Incident') {{
          if (!query) return true;
          return i.name.toLowerCase().includes(query) || (i.description && i.description.toLowerCase().includes(query));
        }}
        if (searchCat === 'Agent') {{
          if (!query) return true;
          return i.agent.name.toLowerCase().includes(query) || (i.agent.architecture && i.agent.architecture.toLowerCase().includes(query));
        }}
        if (searchCat === 'FailureMode') {{
          if (!query) return true;
          return i.failureMode.name.toLowerCase().includes(query) || (i.failureMode.description && i.failureMode.description.toLowerCase().includes(query));
        }}
        if (searchCat === 'Mitigation') {{
          if (!query) return true;
          return i.mitigation.name.toLowerCase().includes(query) || (i.mitigation.strategy && i.mitigation.strategy.toLowerCase().includes(query));
        }}
        if (searchCat === 'FinancialLoss') {{
          if (!query) return true;
          return String(i.financialLoss.amount).includes(query);
        }}

        if (!query) return true;
        return i.name.toLowerCase().includes(query) ||
               (i.description && i.description.toLowerCase().includes(query)) ||
               i.agent.name.toLowerCase().includes(query) ||
               (i.agent.architecture && i.agent.architecture.toLowerCase().includes(query)) ||
               i.failureMode.name.toLowerCase().includes(query) ||
               i.mitigation.name.toLowerCase().includes(query) ||
               String(i.financialLoss.amount).includes(query);
      }});

      if (filtered.length === 0) {{
        container.innerHTML = '<p class="text-zinc-500 italic col-span-3 text-center py-10">No matching incidents found for the selected filter.</p>';
        return;
      }}

      filtered.forEach((inc, idx) => {{
        const sevClass = inc.severity === 'Critical' 
          ? 'bg-rose-500/10 text-rose-300 border border-rose-500/20' 
          : inc.severity === 'High' 
            ? 'bg-amber-500/10 text-amber-300 border border-amber-500/20' 
            : 'bg-sky-500/10 text-sky-300 border border-sky-500/20';

        const sevDot = inc.severity === 'Critical' 
          ? 'bg-rose-400' 
          : inc.severity === 'High' 
            ? 'bg-amber-400' 
            : 'bg-sky-400';

        const delay = Math.min(idx * 35, 500);

        container.innerHTML += `
          <div class="glass-card card-animate p-5 rounded-xl flex flex-col justify-between space-y-4" style="animation-delay: ${{delay}}ms">
            <div class="space-y-3">
              <div class="flex items-start justify-between gap-2">
                <div class="space-y-1">
                  <span class="badge ${{sevClass}}">
                    <span class="w-1.5 h-1.5 rounded-full ${{sevDot}}"></span>
                    ${{inc.severity}} Severity
                  </span>
                  <h3 class="font-semibold text-zinc-100 text-sm leading-snug pt-1">${{inc.name}}</h3>
                  <p class="text-[11px] text-zinc-400 mono">${{inc.date}} · ${{inc.sourceName}}</p>
                </div>
                <span class="text-amber-400 font-mono font-medium text-xs bg-amber-400/10 px-2 py-1 rounded-md border border-amber-400/20 shrink-0">
                  $${{(inc.financialLoss.amount).toLocaleString()}}
                </span>
              </div>

              <p class="text-xs text-zinc-300 leading-relaxed bg-zinc-900/60 p-3 rounded-lg border border-white/5">${{inc.description}}</p>

              <div class="space-y-1.5 text-[11px]">
                <div class="p-2.5 rounded-lg bg-zinc-900/70 border border-white/5 transition hover:border-white/10">
                  <span class="text-zinc-500 block text-[10px] uppercase font-mono font-medium">Involved Agent</span>
                  <span class="text-sky-300 font-medium">${{inc.agent.name}}</span>
                  <span class="text-zinc-400 block text-[10px] mt-0.5">${{inc.agent.architecture}}</span>
                </div>
                <div class="p-2.5 rounded-lg bg-zinc-900/70 border border-white/5 transition hover:border-white/10">
                  <span class="text-zinc-500 block text-[10px] uppercase font-mono font-medium">Failure Mode</span>
                  <span class="text-amber-300 font-medium">${{inc.failureMode.name}}</span>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/20 border border-emerald-800/30 transition hover:border-emerald-700/40">
                  <span class="text-emerald-400 block text-[10px] uppercase font-mono font-medium">Verified Mitigation</span>
                  <span class="text-emerald-200 font-medium">${{inc.mitigation.name}}</span>
                </div>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="pt-3 border-t border-white/5 flex items-center justify-between gap-2">
              <button onclick="openPostMortemModal('${{inc.id}}')" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-zinc-200 hover:text-white border border-white/10 text-xs font-medium transition active:scale-95">
                Read Post-Mortem →
              </button>
              <div class="flex items-center space-x-1.5">
                <a href="${{inc.sourceEvidenceLink}}" target="_blank" rel="noopener" class="p-1.5 rounded-lg bg-zinc-900 hover:bg-zinc-800 text-zinc-400 hover:text-zinc-200 border border-white/5 transition active:scale-90" title="Open Source Link">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                </a>
                <button onclick="focusIncidentInGraph('${{inc.id}}')" class="px-2.5 py-1.5 rounded-lg bg-zinc-900 hover:bg-zinc-800 text-zinc-300 hover:text-white text-xs border border-white/5 transition active:scale-95" title="Focus in 3D">
                  3D &uarr;
                </button>
              </div>
            </div>
          </div>
        `;
      }});
    }}

    function focusIncidentInGraph(id) {{
      const node = nodeMap[id];
      if (node) {{
        flyToNode(node);
      }}
    }}

    // -------------------------------------------------------------------------
    // POST-MORTEM DOSSIER MODAL LOGIC
    // -------------------------------------------------------------------------
    function openPostMortemModal(incidentId) {{
      const inc = incidents.find(i => i.id === incidentId);
      if (!inc) return;

      document.getElementById('pm-title').innerText = inc.name;
      document.getElementById('pm-date').innerText = inc.date;
      document.getElementById('pm-severity-badge').innerText = `${{inc.severity}} Severity`;
      document.getElementById('pm-source-badge').innerText = inc.sourceName || 'Verified Report';

      const extLink = document.getElementById('pm-external-link');
      if (inc.isFromGeo || (inc.id && inc.id.length === 32)) {{
        extLink.href = `https://www.geobrowser.io/space/fb47f7907b4cc91be446bbf9fb51ccad/${{inc.id}}`;
        extLink.innerHTML = `<span>Open on Geo Browser (GRC-20) ↗</span>`;
      }} else {{
        extLink.href = inc.sourceEvidenceLink;
        extLink.innerHTML = `<span>Open Official Filing (${{inc.sourceName || 'Source'}}) ↗</span>`;
      }}

      const pm = inc.postMortem || {{}};

      document.getElementById('pm-body').innerHTML = `
        <!-- Incident Abstract Banner -->
        <div class="p-4 rounded-xl bg-zinc-900/80 border border-white/10 space-y-1.5">
          <div class="text-[10px] uppercase font-mono font-semibold tracking-wider text-zinc-400">Executive Summary</div>
          <p class="text-zinc-200 leading-relaxed">${{pm.summary || inc.description}}</p>
        </div>

        <!-- Metrics Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs mono">
          <div class="p-3 rounded-lg bg-zinc-900/60 border border-white/5">
            <span class="text-zinc-500 block text-[10px]">Financial Impact</span>
            <span class="text-amber-400 font-semibold">$${{(inc.financialLoss.amount).toLocaleString()}}</span>
          </div>
          <div class="p-3 rounded-lg bg-zinc-900/60 border border-white/5">
            <span class="text-zinc-500 block text-[10px]">Severity Class</span>
            <span class="text-rose-400 font-semibold">${{inc.severity}}</span>
          </div>
          <div class="p-3 rounded-lg bg-zinc-900/60 border border-white/5">
            <span class="text-zinc-500 block text-[10px]">Agent</span>
            <span class="text-sky-300 font-semibold truncate block">${{inc.agent.name}}</span>
          </div>
          <div class="p-3 rounded-lg bg-zinc-900/60 border border-white/5">
            <span class="text-zinc-500 block text-[10px]">Evidence</span>
            <span class="text-emerald-400 font-semibold">Verified</span>
          </div>
        </div>

        <!-- Root Cause Analysis -->
        <div class="space-y-1.5">
          <h4 class="text-xs font-semibold text-white flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
            <span>Root Cause &amp; Systemic Vulnerability Mechanism</span>
          </h4>
          <div class="p-3.5 rounded-lg bg-zinc-900/60 border border-white/5 text-zinc-300 whitespace-pre-line leading-relaxed">
            ${{pm.rootCause || inc.failureMode.description}}
          </div>
        </div>

        <!-- Mitigation & Safeguards -->
        <div class="space-y-1.5">
          <h4 class="text-xs font-semibold text-white flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span>Verified Mitigation &amp; Architecture Hardening</span>
          </h4>
          <div class="p-3.5 rounded-lg bg-zinc-900/60 border border-white/5 text-zinc-300 leading-relaxed">
            <p class="font-medium text-emerald-300 mb-1">${{inc.mitigation.name}} (${{inc.mitigation.strategy}})</p>
            <p class="text-zinc-300">${{pm.mitigationDeepDive || inc.mitigation.description}}</p>
          </div>
        </div>

        <!-- Verified External Citations -->
        <div class="space-y-2 pt-2 border-t border-white/[0.08]">
          <div class="text-[10px] uppercase font-mono font-semibold tracking-wider text-zinc-400">Verified Citation Material</div>
          <div class="space-y-1.5">
            <a href="${{inc.sourceEvidenceLink}}" target="_blank" rel="noopener" class="flex items-center justify-between p-2.5 rounded-lg bg-zinc-900/80 hover:bg-zinc-800 border border-white/5 text-zinc-300 hover:text-white transition">
              <span>Primary: ${{inc.sourceName || inc.sourceEvidenceLink}}</span>
              <span class="text-zinc-500">&rarr;</span>
            </a>
            ${{inc.secondaryLink ? `
              <a href="${{inc.secondaryLink}}" target="_blank" rel="noopener" class="flex items-center justify-between p-2.5 rounded-lg bg-zinc-900/80 hover:bg-zinc-800 border border-white/5 text-zinc-300 hover:text-white transition">
                <span>Secondary: ${{inc.secondaryLink}}</span>
                <span class="text-zinc-500">&rarr;</span>
              </a>
            ` : ''}}
          </div>
        </div>
      `;

      document.getElementById('postmortem-modal').classList.remove('hidden');
    }}

    function closePostMortemModal() {{
      document.getElementById('postmortem-modal').classList.add('hidden');
    }}

    // -------------------------------------------------------------------------
    // SYSTEM TRIPLES TABLE
    // -------------------------------------------------------------------------
    function renderTriplesTable() {{
      const tbody = document.getElementById('triples-table-body');
      if (!tbody) return;
      tbody.innerHTML = '';

      const query = ((document.getElementById('search-input')?.value || document.getElementById('catalog-search')?.value) || '').trim().toLowerCase();
      const searchCat = document.getElementById('search-category')?.value || 'all';

      const filteredEdges = edges.filter((e) => {{
        const s = nodeMap[e.source];
        const t = nodeMap[e.target];
        if (!s || !t) return false;

        const matchesCat = (searchCat === 'all' || s.type === searchCat || t.type === searchCat);
        if (!matchesCat) return false;

        if (!query) return true;
        const matchesQuery = s.name.toLowerCase().includes(query) ||
                             t.name.toLowerCase().includes(query) ||
                             e.relation.toLowerCase().includes(query) ||
                             (s.description && s.description.toLowerCase().includes(query)) ||
                             (t.description && t.description.toLowerCase().includes(query));
        return matchesQuery;
      }});

      if (filteredEdges.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="4" class="p-6 text-center text-zinc-500 italic">No matching triples found for the selected filter.</td></tr>';
        return;
      }}

      filteredEdges.forEach((e) => {{
        const s = nodeMap[e.source];
        const t = nodeMap[e.target];
        if (!s || !t) return;

        tbody.innerHTML += `
          <tr class="hover:bg-zinc-800/40 transition">
            <td class="p-3.5 pl-5 font-medium text-zinc-100 flex items-center space-x-2">
              <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:${{s.color}}"></span>
              <span>${{s.name}}</span>
            </td>
            <td class="p-3.5 font-mono text-zinc-400 text-xs">${{e.relation}}</td>
            <td class="p-3.5 font-medium text-zinc-200">
              <span class="w-1.5 h-1.5 rounded-full inline-block mr-1.5" style="background:${{t.color}}"></span>
              <span>${{t.name}}</span>
            </td>
            <td class="p-3.5 pr-5 text-right">
              <button onclick="focusIncidentInGraph('${{s.id}}')" class="px-2.5 py-1 rounded-md bg-zinc-900 hover:bg-zinc-800 text-zinc-300 text-[11px] border border-white/5 transition active:scale-95">
                Inspect 3D
              </button>
            </td>
          </tr>
        `;
      }});
    }}

    // -------------------------------------------------------------------------
    // ADD INCIDENT FORM
    // -------------------------------------------------------------------------
    function openModal() {{
      document.getElementById('add-modal').classList.remove('hidden');
      document.getElementById('form-date').value = new Date().toISOString().split('T')[0];
    }}

    function closeModal() {{
      document.getElementById('add-modal').classList.add('hidden');
    }}

    function handleFormSubmit(e) {{
      e.preventDefault();
      const newId = `inc-${{Date.now().toString().slice(-4)}}`;
      const title = document.getElementById('form-name').value;
      const link = document.getElementById('form-link').value || 'https://incidentdatabase.ai/';

      const newIncident = {{
        id: newId,
        name: title,
        description: 'User-registered incident in FaultGraph.',
        date: document.getElementById('form-date').value,
        severity: document.getElementById('form-severity').value,
        sourceName: 'User Documented Evidence',
        sourceEvidenceLink: link,
        agent: {{
          id: `agent-${{newId}}`,
          name: document.getElementById('form-agent').value,
          architecture: document.getElementById('form-arch').value || 'Autonomous Tool Calling Agent',
          description: 'Autonomous agent component.'
        }},
        failureMode: {{
          id: `fm-${{newId}}`,
          name: document.getElementById('form-failure').value,
          description: 'Identified root cause flaw.'
        }},
        mitigation: {{
          id: `mit-${{newId}}`,
          name: document.getElementById('form-mitigation').value,
          strategy: 'Active Defensive Guardrail',
          description: 'Pre-flight verified defense.'
        }},
        financialLoss: {{
          id: `loss-${{newId}}`,
          amount: Number(document.getElementById('form-loss').value) || 50000,
          currency: 'USD',
          description: 'Estimated financial impact'
        }},
        postMortem: {{
          summary: `Registered incident: ${{title}}`,
          rootCause: `User reported vulnerability: ${{document.getElementById('form-failure').value}}`,
          impact: `Recorded loss: $${{(Number(document.getElementById('form-loss').value) || 50000).toLocaleString()}}`,
          mitigationDeepDive: `Implemented countermeasure: ${{document.getElementById('form-mitigation').value}}`
        }}
      }};

      incidents.unshift(newIncident);
      saveIncidents();
      buildGraphData();
      closeModal();
      showToast('New Triples successfully appended to Knowledge Graph');
      flyToNode(nodeMap[newId]);
    }}

    // Initialize application
    try {{
      localStorage.removeItem('faultgraph-theme');
      document.body.classList.remove('theme-light');
    }} catch (e) {{}}
    loadIncidents();
    resizeCanvas();
    buildGraphData();
    animate();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully written updated animated index.html and app/index.html")
print(f"File size: {len(new_html)} bytes")

#!/usr/bin/env python3
"""
Hacker Terminal GIF Generator for GitHub Profile
Generates a retro hacker-style terminal animation with GitHub stats.
"""

import gifos
import gifos.utils

# ─── Configuration ───────────────────────────────────────────────
USER_NAME = "brkNx"
DISPLAY_NAME = "Berkan Ünal"
TERMINAL_WIDTH = 520
TERMINAL_HEIGHT = 320
XPAD = 8
YPAD = 8

# ─── ANSI Colors (Matrix/Hacker theme) ──────────────────────────
GREEN = "\x1b[32m"
RED = "\x1b[31m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
GRAY = "\x1b[90m"
BOLD = "\x1b[1m"
RESET = "\x1b[0m"


def hold(t, n):
    """Hold current frame by cloning it n times."""
    t.clone_frame(count=n)


def main():
    t = gifos.Terminal(
        width=TERMINAL_WIDTH,
        height=TERMINAL_HEIGHT,
        xpad=XPAD,
        ypad=YPAD,
    )
    t.set_fps(12)
    t.toggle_show_cursor(False)

    row = 1

    # ═══ Phase 1: BIOS Boot Screen ═══════════════════════════════
    t.gen_text(text=f"{BOLD}{RED}BRKN BIOS v3.14.159{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{GRAY}Copyright (C) 2026, BRKN Softwares Inc.{RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{CYAN}Hacker Terminal ReadMe, Rev 2026{RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{WHITE}Krypton(tm) CPUBRK - 5.0GHz{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{WHITE}Memory Test: 65536 MB{RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{YELLOW}Press DEL to enter SETUP, ESC to cancel Memory Test{RESET}", row_num=row, contin=True)
    hold(t, 10)

    # ═══ Phase 2: Boot Sequence ══════════════════════════════════
    t.clear_frame()
    row = 1

    boot_lines = [
        f"{GREEN}[  OK  ]{RESET} Started BRKN Security Module.",
        f"{GREEN}[  OK  ]{RESET} Reached target Graphical Interface.",
        f"{GREEN}[  OK  ]{RESET} Started GNOME Display Manager.",
        f"{GREEN}[  OK  ]{RESET} Network Manager started.",
        f"{GREEN}[  OK  ]{RESET} Started OpenSSH server daemon.",
        f"{YELLOW}[ WARN ]{RESET} Root password login disabled.",
        f"{GREEN}[  OK  ]{RESET} Multi-User System reached.",
        f"{GREEN}[  OK  ]{RESET} BRKN Terminal Emulator started.",
    ]

    for i, line in enumerate(boot_lines):
        t.gen_text(text=line, row_num=row, contin=True)
        row += 1
        hold(t, 3)

    hold(t, 6)

    # ═══ Phase 3: Login ══════════════════════════════════════════
    t.clear_frame()
    row = 1

    t.gen_text(text=f"{BOLD}{GREEN}BRKN OS 26.04 LTS (GNU/Linux 6.8.0-brkn){RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{WHITE}brkn login: {GREEN}{USER_NAME}{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{WHITE}Password: {GRAY}********{RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{GREEN}Last login: {YELLOW}Thu Aug 27 14:09:51 2026{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{GRAY}Welcome to BRKN OS. Type 'help' for available commands.{RESET}", row_num=row, contin=True)
    hold(t, 8)

    # ═══ Phase 4: Neofetch ═══════════════════════════════════════
    t.clear_frame()
    row = 1

    # Fetch GitHub stats
    github_stats = None
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name=USER_NAME)
    except (SystemExit, Exception) as e:
        print(f"[!] GitHub stats unavailable (set GITHUB_TOKEN for live stats)")

    # ASCII Art Logo
    logo_lines = [
        f"{GREEN}    _______   {RESET}",
        f"{GREEN}   /       \\  {RESET}",
        f"{GREEN}  /  BRKN   \\ {RESET}",
        f"{GREEN} /           \\{RESET}",
        f"{GREEN}|  > Terminal |{RESET}",
        f"{GREEN} \\           /{RESET}",
        f"{GREEN}  \\_________/ {RESET}",
    ]

    # Info lines
    info_lines = [
        f"{BOLD}{GREEN}{DISPLAY_NAME}{RESET}@{GREEN}{USER_NAME}{RESET}",
        f"{GRAY}------------------{RESET}",
        f"{GREEN}OS:{RESET} BRKN OS 26.04 LTS",
        f"{GREEN}Host:{RESET} GitHub Profile",
        f"{GREEN}Kernel:{RESET} 6.8.0-brkn",
        f"{GREEN}Uptime:{RESET} since 2026",
        f"{GREEN}Packages:{RESET} 47 (repos)",
        f"{GREEN}Shell:{RESET} zsh 5.9",
        f"{GREEN}Terminal:{RESET} BRKN-Term",
        f"{GREEN}CPU:{RESET} Krypton CPUBRK @ 5.0GHz",
        f"{GREEN}Memory:{RESET} 65536MiB / 131072MiB",
    ]

    if github_stats:
        info_lines.append(f"{GRAY}------------------{RESET}")
        info_lines.append(f"{GREEN}GitHub:{RESET} @{USER_NAME}")
        info_lines.append(f"{GREEN}Stars:{RESET} {YELLOW}{github_stats.total_stargazers}{RESET}")
        info_lines.append(f"{GREEN}Followers:{RESET} {CYAN}{github_stats.total_followers}{RESET}")
        info_lines.append(f"{GREEN}Commits:{RESET} {CYAN}{github_stats.total_commits_all_time}{RESET}")
        info_lines.append(f"{GREEN}PRs:{RESET} {CYAN}{github_stats.total_pull_requests_made}{RESET}")
        info_lines.append(f"{GREEN}Repos:{RESET} {CYAN}{github_stats.total_repo_contributions}{RESET}")

    # Render side by side
    max_lines = max(len(logo_lines), len(info_lines))
    for i in range(max_lines):
        left = logo_lines[i] if i < len(logo_lines) else " " * 20
        right = info_lines[i] if i < len(info_lines) else ""
        t.gen_text(text=f"{left}  {right}", row_num=row, contin=True)
        row += 1

    row += 1

    # Color palette
    t.gen_text(text=f"{BOLD}Color Palette:{RESET}", row_num=row, contin=True)
    row += 1
    palette = (
        f"{RED}### {RESET}{GREEN}### {RESET}{YELLOW}### "
        f"{RESET}{CYAN}### {RESET}{WHITE}### {RESET}{GRAY}###{RESET}"
    )
    t.gen_text(text=palette, row_num=row, contin=True)
    row += 1
    row += 1

    # System info bar
    t.gen_text(text=f"{GRAY}+----------------------------------------------+{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(
        text=f"{GRAY}|{RESET} {GREEN}Files:{RESET} 1.2GB  {GREEN}CPU:{RESET} 12%  {GREEN}RAM:{RESET} 50%  {GREEN}NET:{RESET} ^/ v {GRAY}|{RESET}",
        row_num=row, contin=True,
    )
    row += 1
    t.gen_text(text=f"{GRAY}+----------------------------------------------+{RESET}", row_num=row, contin=True)
    hold(t, 12)

    # ═══ Phase 5: Command Prompt ═════════════════════════════════
    t.clear_frame()
    row = 1

    prompt = f"{GREEN}{USER_NAME}@brkn-os{RESET}:{BLUE}~{RESET}$ "

    commands = [
        ("neofetch --ascii", f"{GREEN}... system info displayed above ...{RESET}"),
        ("cat /etc/motd", f"{BOLD}{GREEN}  Welcome to BRKN OS - Build. Break. Repeat.{RESET}"),
        ("curl -s api.github.com/users/brkn | jq .name", f'"{DISPLAY_NAME}"'),
        ("echo $USER", USER_NAME),
        ("date", "Thu Aug 27 14:09:51 IST 2026"),
        ("uname -a", "Linux brkn-os 6.8.0-brkn #1 SMP x86_64 GNU/Linux"),
    ]

    for cmd, output in commands:
        t.gen_text(text=f"{prompt}{cmd}", row_num=row, contin=True)
        row += 1
        t.gen_text(text=output, row_num=row, contin=True)
        row += 1
        hold(t, 4)

    # Final prompt with cursor
    t.toggle_show_cursor(True)
    t.toggle_blink_cursor(True)
    t.gen_text(text=f"{prompt}", row_num=row, contin=True)

    # ═══ Generate GIF ════════════════════════════════════════════
    print("[*] Generating GIF frames...")
    t.gen_gif()
    print("[✓] GIF generated: output.gif")


if __name__ == "__main__":
    main()

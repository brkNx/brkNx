#!/usr/bin/env python3
"""
Hacker Terminal GIF Generator for GitHub Profile
Generates a retro hacker-style terminal animation with GitHub stats.
"""

import gifos
import gifos.utils

# ─── Configuration ───────────────────────────────────────────────
USER_NAME = "brkNx"
DISPLAY_NAME = "brkNx"
TERMINAL_WIDTH = 960
TERMINAL_HEIGHT = 540
XPAD = 16
YPAD = 16

# ─── ANSI Colors (Matrix/Hacker theme) ──────────────────────────
GREEN = "\x1b[32m"
BRIGHT_GREEN = "\x1b[92m"
RED = "\x1b[31m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
GRAY = "\x1b[90m"
BOLD = "\x1b[1m"
RESET = "\x1b[0m"


def hold(t, n):
    t.clone_frame(count=n)


def main():
    t = gifos.Terminal(
        width=TERMINAL_WIDTH,
        height=TERMINAL_HEIGHT,
        xpad=XPAD,
        ypad=YPAD,
    )
    t.set_fps(15)
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
    hold(t, 15)

    # ═══ Phase 2: Memory Count ═══════════════════════════════════
    t.clear_frame()
    row = 1
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
    mem_count = [8192, 16384, 32768, 49152, 65536]
    for m in mem_count:
        t.gen_text(text=f"{WHITE}Memory Test: {m} MB{RESET}", row_num=row, contin=True)
        hold(t, 3)
    row += 1
    row += 1
    t.gen_text(text=f"{GREEN}Memory Test Passed.{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{YELLOW}Press DEL to enter SETUP, ESC to cancel Memory Test{RESET}", row_num=row, contin=True)
    hold(t, 8)

    # ═══ Phase 3: Boot Sequence ══════════════════════════════════
    t.clear_frame()
    row = 1

    boot_lines = [
        (f"{GREEN}[  OK  ]{RESET} Started BRKN Security Module.", 3),
        (f"{GREEN}[  OK  ]{RESET} Reached target Graphical Interface.", 3),
        (f"{GREEN}[  OK  ]{RESET} Started GNOME Display Manager.", 3),
        (f"{GREEN}[  OK  ]{RESET} Network Manager started.", 2),
        (f"{GREEN}[  OK  ]{RESET} Started OpenSSH server daemon.", 2),
        (f"{YELLOW}[ WARN ]{RESET} Root password login disabled.", 4),
        (f"{GREEN}[  OK  ]{RESET} Multi-User System reached.", 2),
        (f"{GREEN}[  OK  ]{RESET} BRKN Terminal Emulator started.", 2),
        (f"{GREEN}[  OK  ]{RESET} Docker daemon started.", 2),
        (f"{GREEN}[  OK  ]{RESET} System logger started.", 2),
        (f"{GREEN}[  OK  ]{RESET} Time synchronization started.", 2),
        (f"{GREEN}[  OK  ]{RESET} BRKN OS ready.{RESET}", 5),
    ]

    for i, (line, delay) in enumerate(boot_lines):
        t.gen_text(text=line, row_num=row, contin=True)
        row += 1
        hold(t, delay)

    hold(t, 8)

    # ═══ Phase 4: Login ══════════════════════════════════════════
    t.clear_frame()
    row = 1

    t.gen_text(text=f"{BOLD}{GREEN}BRKN OS 26.04 LTS (GNU/Linux 6.8.0-brkn){RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{GRAY}brkn login: {RESET}", row_num=row, contin=True)
    hold(t, 5)
    t.gen_text(text=f"{GRAY}brkn login: {GREEN}{USER_NAME}{RESET}", row_num=row, contin=True)
    row += 1
    hold(t, 3)
    t.gen_text(text=f"{WHITE}Password: {GRAY}********{RESET}", row_num=row, contin=True)
    row += 1
    hold(t, 5)
    row += 1
    t.gen_text(text=f"{GREEN}Last login: {YELLOW}Thu Aug 27 14:09:51 2026 from 192.168.1.42{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(text=f"{GRAY}Welcome to BRKN OS. Type 'help' for available commands.{RESET}", row_num=row, contin=True)
    hold(t, 10)

    # ═══ Phase 5: Neofetch ═══════════════════════════════════════
    t.clear_frame()
    row = 1

    # Fetch GitHub stats
    github_stats = None
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name=USER_NAME)
    except (SystemExit, Exception):
        print(f"[!] GitHub stats unavailable")

    # ASCII Art Logo - bigger and better
    logo_lines = [
        f"{GREEN}         _____  {RESET}",
        f"{GREEN}        /     \\ {RESET}",
        f"{GREEN}       / () () \\{RESET}",
        f"{GREEN}      |   __   |{RESET}",
        f"{GREEN}      |  |  |  |{RESET}",
        f"{GREEN}   ___|  |__|  |___{RESET}",
        f"{GREEN}  /    BRKN OS    \\{RESET}",
        f"{GREEN} /________________\\{RESET}",
    ]

    # Info lines
    info_lines = [
        f"{BOLD}{GREEN}{DISPLAY_NAME}{RESET}@{GREEN}brkn-os{RESET}",
        f"{GRAY}------------------------{RESET}",
        f"{GREEN}OS:{RESET} BRKN OS 26.04 LTS x86_64",
        f"{GREEN}Host:{RESET} GitHub Profile",
        f"{GREEN}Kernel:{RESET} 6.8.0-brkn",
        f"{GREEN}Uptime:{RESET} 365 days, 4 hours",
        f"{GREEN}Packages:{RESET} 47 (repos)",
        f"{GREEN}Shell:{RESET} zsh 5.9",
        f"{GREEN}Terminal:{RESET} BRKN-Term v2.0",
        f"{GREEN}CPU:{RESET} Krypton CPUBRK @ 5.0GHz",
        f"{GREEN}GPU:{RESET} NVIDIA RTX 5090 24GB",
        f"{GREEN}Memory:{RESET} 65536MiB / 131072MiB",
    ]

    if github_stats:
        info_lines.append(f"{GRAY}------------------------{RESET}")
        info_lines.append(f"{GREEN}GitHub:{RESET} @{USER_NAME}")
        info_lines.append(f"{GREEN}Stars:{RESET} {YELLOW}{github_stats.total_stargazers}{RESET}")
        info_lines.append(f"{GREEN}Followers:{RESET} {CYAN}{github_stats.total_followers}{RESET}")
        info_lines.append(f"{GREEN}Commits:{RESET} {CYAN}{github_stats.total_commits_all_time}{RESET}")
        info_lines.append(f"{GREEN}PRs:{RESET} {CYAN}{github_stats.total_pull_requests_made}{RESET}")
        info_lines.append(f"{GREEN}Repos:{RESET} {CYAN}{github_stats.total_repo_contributions}{RESET}")

    # Render side by side
    max_lines = max(len(logo_lines), len(info_lines))
    for i in range(max_lines):
        left = logo_lines[i] if i < len(logo_lines) else " " * 25
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
    t.gen_text(text=f"{GRAY}+-----------------------------------------------+{RESET}", row_num=row, contin=True)
    row += 1
    t.gen_text(
        text=f"{GRAY}|{RESET} {GREEN}Files:{RESET} 1.2TB  {GREEN}CPU:{RESET} 12%  {GREEN}RAM:{RESET} 50%  {GREEN}NET:{RESET} ^12MB/s v8MB/s {GRAY}|{RESET}",
        row_num=row, contin=True,
    )
    row += 1
    t.gen_text(text=f"{GRAY}+-----------------------------------------------+{RESET}", row_num=row, contin=True)
    hold(t, 15)

    # ═══ Phase 6: Command Prompt ═════════════════════════════════
    t.clear_frame()
    row = 1

    prompt = f"{GREEN}{USER_NAME}@brkn-os{RESET}:{BLUE}~{RESET}$ "

    commands = [
        ("neofetch --ascii", f"{GREEN}... system info displayed above ...{RESET}"),
        ("cat /etc/motd", f"{BOLD}{GREEN}  Welcome to BRKN OS - Build. Break. Repeat.{RESET}"),
        ("curl -s api.github.com/users/brkNx | jq .name", f'"{DISPLAY_NAME}"'),
        ("echo $USER", USER_NAME),
        ("date", "Thu Aug 27 14:09:51 IST 2026"),
        ("uname -a", "Linux brkn-os 6.8.0-brkn #1 SMP x86_64 GNU/Linux"),
        ("uptime", "14:09:51 up 365 days, 4:23, 1 user, load average: 0.42, 0.37, 0.28"),
        ("df -h /", "/dev/sda1  1.2T  420G  780G  35% /"),
        ("free -h", "              total    used    free   shared  buff/cache  available"),
        ("", "Mem:          128Gi   64Gi   32Gi   2.0Gi      32Gi       62Gi"),
    ]

    for cmd, output in commands:
        t.gen_text(text=f"{prompt}{cmd}", row_num=row, contin=True)
        row += 1
        t.gen_text(text=output, row_num=row, contin=True)
        row += 1
        hold(t, 3)

    hold(t, 5)

    # ═══ Phase 7: Matrix Rain Effect ═════════════════════════════
    t.clear_frame()
    row = 1

    matrix_chars = "01"
    for frame in range(20):
        t.clear_frame()
        row = 1
        for r in range(20):
            line = ""
            for c in range(60):
                import random
                if random.random() < 0.3:
                    line += f"{GREEN}{random.choice(matrix_chars)}{RESET}"
                else:
                    line += " "
            t.gen_text(text=line, row_num=row, contin=True)
            row += 1
        hold(t, 1)

    # ═══ Phase 8: Final Screen ═══════════════════════════════════
    t.clear_frame()
    row = 1

    # Big ASCII art
    big_art = [
        f"{BOLD}{GREEN}    ____  ____  ____  ____  ____  ____  ____  ____{RESET}",
        f"{BOLD}{GREEN}   |    ||    ||    ||    ||    ||    ||    ||    |{RESET}",
        f"{BOLD}{GREEN}   | B  || R  || K  || N  | OS |    ||    ||    |{RESET}",
        f"{BOLD}{GREEN}   |____||____||____||____||____||____||____||____|{RESET}",
        f"{BOLD}{GREEN}   |    ||    ||    ||    ||    ||    ||    ||    |{RESET}",
        f"{BOLD}{GREEN}   | B  || R  || K  || N  |    |    ||    ||    |{RESET}",
        f"{BOLD}{GREEN}   |____||____||____||____||____||____||____||____|{RESET}",
    ]

    for line in big_art:
        t.gen_text(text=line, row_num=row, contin=True)
        row += 1

    row += 1
    t.gen_text(text=f"{BOLD}{GREEN}Build. Break. Repeat.{RESET}", row_num=row, contin=True)
    row += 1
    row += 1
    t.gen_text(text=f"{GRAY}Generated using github-readme-terminal{RESET}", row_num=row, contin=True)
    hold(t, 20)

    # ═══ Generate GIF ════════════════════════════════════════════
    print("[*] Generating GIF frames...")
    t.gen_gif()
    print("[+] GIF generated: output.gif")


if __name__ == "__main__":
    main()

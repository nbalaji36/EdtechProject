# backend/story_data.py

game_data = {
    "startScene": "intro_1",
    "scenes": {
        "intro_1": {
            "title": "Graduation & First Job Offer",
            "text": (
                "You’ve just graduated and landed your first full-time job making $65,000/year. "
                "Your employer offers a 401(k) with a 4% match. You’ve heard of Roth IRAs, "
                "but never opened one. This is your first chance to decide what Future You looks like."
            ),
            "question": "What do you do first?",
            "choices": [
                {
                    "label": "Contribute 4% to get the full 401(k) employer match",
                    "next": "scene_match_explain",
                    "effects": {"literacy": 6},
                    "explanation": "Grabbing the match is one of the highest guaranteed returns you’ll ever see."
                },
                {
                    "label": "Open a Roth IRA and contribute $100/month",
                    "next": "scene_roth_intro",
                    "effects": {"literacy": 5},
                    "explanation": "Starting tax-free growth early is a powerful long-term move."
                },
                {
                    "label": "Skip retirement for now; focus on rent, loans, and fun",
                    "next": "scene_skip_warning",
                    "effects": {"literacy": -3},
                    "explanation": "Common and understandable—but delay has a real compounding cost."
                }
            ]
        },

        "scene_match_explain": {
            "title": "Unlocking the Match",
            "text": (
                "You enroll at 4% and your employer matches 4%. Every paycheck, 8% of your salary "
                "is quietly invested for Future You."
            ),
            "question": "What do you want to understand next?",
            "choices": [
                {
                    "label": "Compare Roth vs Traditional 401(k) options",
                    "next": "scene_rothvstrad",
                    "effects": {"literacy": 4},
                    "explanation": "Understanding taxes turns a good habit into a smart strategy."
                },
                {
                    "label": "Stay on autopilot for now",
                    "next": "scene_autopilot",
                    "effects": {"literacy": 1},
                    "explanation": "You’re investing, but might miss optimization opportunities."
                }
            ]
        },

        "scene_roth_intro": {
            "title": "Starting Your Roth IRA",
            "text": (
                "You open a Roth IRA and set up an automatic $100/month contribution. "
                "It feels good to be doing something, even if you haven’t touched the 401(k) yet."
            ),
            "question": "What’s on your mind?",
            "choices": [
                {
                    "label": "Wait, am I missing free money from the 401(k) match?",
                    "next": "scene_match_explain",
                    "effects": {"literacy": 3},
                    "explanation": "Ideal order: grab the match, then add Roth on top if you can."
                },
                {
                    "label": "Stick with Roth only; I’ll revisit later",
                    "next": "scene_roth_only_path",
                    "effects": {"literacy": 1},
                    "explanation": "You’re investing (good), but leaving some benefits unused."
                }
            ]
        },

        "scene_skip_warning": {
            "title": "The Cost of Waiting",
            "text": (
                "Months pass. A friend shows you a chart: starting with $100/month at 22 vs 32 "
                "creates a massive gap by retirement. You feel a quiet pit in your stomach."
            ),
            "question": "How do you respond?",
            "choices": [
                {
                    "label": "Show me the numbers. I want to restart smarter.",
                    "next": "scene_intro_reset",
                    "effects": {"literacy": 6},
                    "explanation": "Recognizing the cost of delay is a key literacy breakthrough."
                },
                {
                    "label": "It’s overwhelming. Keep putting it off.",
                    "next": "scene_bad_outcome",
                    "effects": {"literacy": -4},
                    "explanation": "Avoidance is realistic—but Future You will feel the impact."
                }
            ]
        },

        "scene_rothvstrad": {
            "title": "Roth vs Traditional 401(k)",
            "text": (
                "You learn: Roth = pay tax now, tax-free later. Traditional = tax break now, taxed later. "
                "Early in your career, your tax rate is often lower than it will be later."
            ),
            "question": "Given that, which option do you choose for most of your contributions?",
            "choices": [
                {
                    "label": "Roth 401(k) for tax-free withdrawals later",
                    "next": "scene_midgame_growth",
                    "effects": {"literacy": 4},
                    "explanation": "Great for early-career earners expecting higher future income."
                },
                {
                    "label": "Traditional 401(k) to reduce taxes today",
                    "next": "scene_midgame_growth",
                    "effects": {"literacy": 3},
                    "explanation": "Also valid. The key is making an intentional, informed choice."
                }
            ]
        },

        "scene_autopilot": {
            "title": "Autopilot Mode",
            "text": (
                "You’re contributing to your 401(k), but you picked the first fund on the list. "
                "You’re not sure about fees or risk."
            ),
            "question": "Next step?",
            "choices": [
                {
                    "label": "Learn what a target-date fund is",
                    "next": "scene_targetdate",
                    "effects": {"literacy": 4},
                    "explanation": "Target-date funds auto-adjust risk and are a strong default."
                },
                {
                    "label": "Stay in the random fund and hope for the best",
                    "next": "scene_midgame_growth",
                    "effects": {"literacy": 0},
                    "explanation": "Better than nothing, but might mean higher risk or unnecessary fees."
                }
            ]
        },

        "scene_intro_reset": {
            "title": "Rewind With Insight",
            "text": (
                "Seeing the power of compounding, you decide to act intentionally instead of avoiding. "
                "You’re ready to design a plan that Future You would thank you for."
            ),
            "question": "How do you restart?",
            "choices": [
                {
                    "label": "Start 4% 401(k) contributions to capture the match",
                    "next": "scene_match_explain",
                    "effects": {"literacy": 4},
                    "explanation": "Correcting early prevents long-term regret."
                },
                {
                    "label": "Open a Roth IRA AND plan to add the 401(k) match soon",
                    "next": "scene_roth_intro",
                    "effects": {"literacy": 4},
                    "explanation": "Stacking accounts is powerful once the basics are in place."
                }
            ]
        },

        "scene_bad_outcome": {
            "title": "Flash-Forward: Age 45",
            "text": (
                "You’re earning well, but your retirement savings are thin. "
                "Catching up now requires painfully large monthly contributions."
            ),
            "question": "What now?",
            "choices": [
                {
                    "label": "Replay from the start and see how earlier choices change this outcome.",
                    "next": "intro_1",
                    "effects": {"literacy": 5},
                    "explanation": "The simulation lets you fail safely, reflect, and choose differently."
                }
            ]
        },

        "scene_targetdate": {
            "title": "Target-Date Fund 101",
            "text": (
                "You switch into a low-fee target-date fund aligned with your expected retirement year. "
                "Risky now, safer later—without constant tweaking."
            ),
            "question": "Ready to see how this plays out over time?",
            "choices": [
                {
                    "label": "Fast-forward a few years",
                    "next": "scene_midgame_growth",
                    "effects": {"literacy": 3},
                    "explanation": "You’ve paired automation with a sensible long-term strategy."
                }
            ]
        },

        "scene_roth_only_path": {
            "title": "Solo Roth Strategy",
            "text": (
                "Your Roth IRA grows slowly but steadily. Then a coworker mentions their 401(k) match, "
                "and you realize you’ve left free money on the table."
            ),
            "question": "What do you adjust?",
            "choices": [
                {
                    "label": "Add 4% to 401(k) to capture the match while keeping the Roth",
                    "next": "scene_match_explain",
                    "effects": {"literacy": 4},
                    "explanation": "Combining match + Roth is a powerhouse setup in your 20s."
                }
            ]
        },

        "scene_midgame_growth": {
            "title": "Fast-Forward: Age 30",
            "text": (
                "Because you started in your 20s, you’ve built a meaningful base instead of starting from zero. "
                "The exact number depends on your path—but the habit is locked in."
            ),
            "question": "How would you like to consolidate what you’ve learned?",
            "choices": [
                {
                    "label": "Show me a summary of my path and key lessons",
                    "next": "scene_summary",
                    "effects": {"literacy": 3},
                    "explanation": "Reflection turns scattered decisions into a mental model."
                }
            ]
        },

        "scene_summary": {
            "title": "Your Financial Story So Far",
            "text": (
                "Here’s where your choices have led you. Compare this timeline with other runs to see how "
                "small early decisions compound into very different futures."
            ),
            "question": "What next?",
            "choices": [
                {
                    "label": "Restart and explore a different path",
                    "next": "intro_1",
                    "effects": {},
                    "explanation": "Exploring alternate timelines deepens understanding more than a one-time quiz."
                }
            ]
        }
    }
}

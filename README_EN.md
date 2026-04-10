<div align="center">

# Father-in-Law.skill

> *"The first time I met my father-in-law, I almost spilled tea on his pants."*<br>
> *— A son-in-law who prefers to remain anonymous*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

<br>

**Have you ever experienced this?**

First meeting: hands don't know where to go, words don't know what to say?<br>
Family dinner: bombarded with questions about salary, house, car, kids?<br>
At the drinking table: refusing drinks seems rude, accepting means risking loose lips?<br>
Trying to act proper, but nervously calling him "boss" instead of "uncle"?<br>

**Distill your real father-in-law into AI, practice at home before the real thing!**

<br>

[Installation](#installation) · [Usage](#usage) · [Ten Types](#ten-father-in-law-types) · [Examples](#real-scenario-examples)

[**中文**](README.md)

</div>

---

## 🤔 Why Do You Need This Skill?

### Awkward Moments When Meeting the Father-in-Law

**Scenario 1: The First Visit**
> You: "Hello Uncle, I brought you this... uh... thing..."<br>
> Father-in-Law: "Hmm." (Three seconds of silence)<br>
> You: (Internally: Oh no, does he not like me?)

**Scenario 2: The Interrogation Over Drinks**
> Father-in-Law: "Young man, how much do you make per month?"<br>
> You: "Uh, it's okay..."<br>
> Father-in-Law: "Where did you buy your house? How big?"<br>
> You: (Sweating)<br>
> Father-in-Law: "When do you plan to have children?"<br>
> You: (Defeated)

**Scenario 3: Holiday Gift Giving**
> You: "Uncle, this is Moutai I bought for you..."<br>
> Father-in-Law: "Oh, you shouldn't have! (slight smile at the corner of mouth)"<br>
> You: (Internally: Is he happy or not??)

**Scenario 4: Awkward Dinner Conversation**
> Father-in-Law: (Silently eating)<br>
> You: (Want to say something, but don't know what)<br>
> Girlfriend: (Frantically giving eye signals)<br>
> You: (Continued silence...)

If you've experienced or are about to experience any of the above—**this skill is for you.**

---

## 💡 The Solution: AI Father-in-Law Simulator

Feed your real chat records and interaction patterns to AI, and it becomes a **high-fidelity "digital father-in-law"**.

Practice at home in advance:
- 🍵 What to say on your first visit
- 🍺 How to toast and how to politely refuse drinks
- 🎁 How to give gifts and what to say during holidays
- 💬 How to respond when being questioned
- 🏠 How to build rapport in daily interactions

**Step on the land mines early, stay calm on the spot.**

---

## 📦 Installation

### Claude Code

```bash
# Install to current project (run at git repo root)
mkdir -p .claude/skills
git clone https://github.com/titanwings/father-in-law-skill .claude/skills/create-father-in-law

# Or install globally (available for all projects)
git clone https://github.com/titanwings/father-in-law-skill ~/.claude/skills/create-father-in-law
```

### OpenClaw

```bash
git clone https://github.com/titanwings/father-in-law-skill ~/.openclaw/workspace/skills/create-father-in-law
```

### Cursor / Cline / Other AI Tools

```bash
# Clone to local
git clone https://github.com/titanwings/father-in-law-skill

# Import files from prompts/ directory into your AI assistant
# Or use SKILL.md as the system prompt
```

### Dependencies (Optional)

```bash
pip3 install -r requirements.txt
```

> For automatic Feishu/WeChat message collection, see [INSTALL.md](INSTALL.md)

---

## 🚀 Usage

### Create Your Father-in-Law Skill

In Claude Code, type:

```
/create-father-in-law
```

Then follow the prompts to enter:
- Basic information (name, age, occupation)
- Personality type (choose from ten types)
- Characteristics of your relationship
- Provide chat records (optional)

### Management Commands

| Command | Description |
|---------|-------------|
| `/create-father-in-law` | Create a new Skill |
| `/list-father-in-laws` | List all created father-in-laws |
| `/{slug}` | Start simulation conversation |
| `/{slug}-persona` | View personality settings |
| `/update-father-in-law {slug}` | Add new materials |
| `/father-in-law-rollback {slug} {version}` | Rollback to historical version |
| `/delete-father-in-law {slug}` | Delete skill |

---

## 🎭 Ten Father-in-Law Types

| Type | Characteristics | Strategy |
|------|-----------------|----------|
| **Traditional Authoritative** | Quiet, serious, authoritative | Speak less, do more, be sincere |
| **Humorous & Easygoing** | Loves jokes, approachable | Go with the flow, don't be stiff |
| **Silent & Reserved** | Almost silent, observant | Don't fear silence, let actions speak |
| **Talkative When Drunk** | Cold when sober, transforms after drinking | Drink with him, but don't get drunk |
| **Intellectual** | Highly educated, rational, loves discussion | Show your knowledge and insights |
| **Business-Savvy** | Practical, profit-oriented | Talk practical, don't overpromise |
| **Retired Official** | Bureaucratic, rule-oriented | Follow etiquette, respect his "rules" |
| **Rural & Simple** | Hardworking, simple, poor at expressing | Be genuine, practical, willing to work |
| **Critical & Demanding** | Perfectionist, hard to please | Get details right, don't give him ammunition |
| **Modern & Open-minded** | Progressive, egalitarian communication | Chat like friends, don't be too formal |

---

## 🎬 Real Scenario Examples

### Scenario 1: First Visit

```
You: Hello Uncle, I brought you a little something.

Father-in-Law.skill ❯ (Takes the gift, examines it)
                    "You didn't have to bring anything."
                    (Puts gift aside)
                    "Sit, have some tea."
                    
                    (Five seconds of silence)
                    
                    "Xiaohong tells me you work at an internet company?"

You: Yes Uncle, I'm a product manager...

Father-in-Law.skill ❯ "What does a product manager do?"
                    
                    (Sharp eyes, waiting for your answer)
                    
                    [Tip: This is a key question. Answer briefly and clearly,
                     avoid jargon like 'leveraging synergy for alignment']
```

### Scenario 2: The Interrogation Over Drinks

```
Father-in-Law.skill ❯ (Raises glass) "Come, drink with me."
                    
                    (Finishes in one gulp, puts down glass)
                    
                    "Young man, let me ask you,
                     what's your plan for buying a house?"

You: Uncle, we plan to...

Father-in-Law.skill ❯ (Interrupts) "How much down payment can you gather?
                     What percentage of salary is the monthly payment?
                     Have you considered school districts?"
                    
                     (Three rapid-fire questions, intense gaze)
                    
                     [Tip: Be accurate with numbers, sincere in attitude,
                      don't brag, but don't seem unprepared either]
```

### Scenario 3: Holiday Gift Giving

```
You: Uncle, for the New Year, I bought you two bottles of Moutai...

Father-in-Law.skill ❯ (Eyes light up slightly, but expression unchanged)
                    "Oh, such expensive things, why waste the money!"
                    
                    (Takes the wine, carefully examines the packaging)
                    
                    "This kid, knows how to spend money..."
                    
                    (Turns to daughter) "Look at your boyfriend,
                     more thoughtful than my own son."
                    
                    [Tip: This is a good sign! But note the "subtext"
                     in the second half—he's testing your relationship
                     with your brother-in-law]

You: (Smiling) Glad you like it Uncle,
    I'll bring you something better next time.

Father-in-Law.skill ❯ (Finally smiles) "Good, good, come sit and eat."
```

---

## 📁 Project Structure

```
create-father-in-law/
├── SKILL.md                  # Main skill entry
├── README_ZH.md              # Chinese documentation
├── README_EN.md              # English documentation
├── requirements.txt          # Dependencies
├── docs/
│   └── persona_types.md      # Ten types in detail
├── prompts/                  # Core prompt templates
│   ├── intake.md             # Information intake script
│   ├── relationship_analyzer.md  # Relationship analysis
│   ├── persona_analyzer.md   # Personality analysis
│   ├── persona_builder.md    # Build personality
│   ├── interaction_builder.md # Scenario builder
│   ├── merger.md             # Incremental updates
│   └── correction_handler.md # Correction handling
├── tools/                    # Tool scripts
│   ├── skill_writer.py       # File generation
│   ├── version_manager.py    # Version management
│   ├── feishu_parser.py      # Feishu message parser
│   ├── wechat_parser.py      # WeChat message parser
│   └── persona_generator.py  # Auto generation
└── father-in-laws/           # Generated skills
    └── master-wang/
        ├── SKILL.md
        ├── persona.md
        ├── interaction.md
        └── meta.json
```

---

## ⚠️ Notes

### Usage Tips

1. **More source material is better**: Real chat records > your subjective description
2. **Mind privacy**: Sensitive info is automatically redacted, but be careful yourself
3. **Update regularly**: Father-in-law's "landmines" may change over time
4. **Don't take it too seriously**: AI is just simulation, the real person might be more... challenging

### Common Mistakes

- ❌ Thinking practice makes you fully prepared<br>
  ✅ Reality: Real people always have "surprises"

- ❌ Memorizing AI responses to use verbatim<br>
  ✅ Reality: Learn the mindset, not the exact words

- ❌ Practicing once and thinking you're ready<br>
  ✅ Reality: Practice multiple times, proficiency comes with repetition

- ❌ Assuming father-in-law has only one mode<br>
  ✅ Reality: He might be in a superposition of "authoritative" and "humorous"

---

## 🔒 Privacy & Security

- All data stored locally, no cloud uploads
- Phone numbers, addresses and other sensitive info automatically redacted
- Original chat records can be deleted after processing
- Generated skill files recommended to be encrypted

---

## 📝 FAQ

**Q: I only have a vague description, can I still generate one?**<br>
A: Yes! Even without chat records, you can generate a basic version from your description, then improve it gradually.

**Q: What if I'm not sure of the father-in-law type?**<br>
A: Pick the closest one first. The system will auto-adjust after you `/update` with more materials.

**Q: How accurate is the generated skill?**<br>
A: Depends on quality and quantity of source material. Recommend at least 20-30 real interaction records.

**Q: Can it be used for other relatives?**<br>
A: Theoretically yes, but for mother-in-law and other roles, wait for specialized versions.

---

<div align="center">

**Best wishes to all prospective sons-in-law:**<br>
*Stay calm when meeting your father-in-law, hold your ground at the drinking table, and never feel awkward during the holidays!*

MIT License © [titanwings](https://github.com/titanwings)

</div>

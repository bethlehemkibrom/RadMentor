
from pathlib import Path

path = Path("app.py")

text = path.read_text()

text = text.replace(
"""
height:210px;
""",
"""
min-height:210px;
height:auto;
overflow:hidden;
word-wrap:break-word;
"""
)

text = text.replace(
"""
.hero-text {{
font-size:22px;
color:#475569;
max-width:800px;
margin:auto;
}}
""",
"""
.hero-text {{
font-size:clamp(16px,2.5vw,22px);
color:#475569;
max-width:800px;
margin:auto;
line-height:1.6;
word-wrap:break-word;
}}
"""
)

path.write_text(text)

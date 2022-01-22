mkdir pages/components/$1
touch pages/components/$1/$1.md
cat > pages/components/$1.py << EOL
import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__)

layout = convert_md_to_dash_layout("components/$1/$1.md")

EOL

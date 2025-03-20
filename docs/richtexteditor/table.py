import dash_mantine_components as dmc

table = """
    <table>
      <tbody>
        <tr>
          <th>Name</th>
          <th colspan="3">Description</th>
        </tr>
        <tr>
          <td>Cyndi Lauper</td>
          <td>Singer</td>
          <td>Songwriter</td>
          <td>Actress</td>
        </tr>
        <tr>
          <td>Bruce Springsteen</td>
          <td>Singer</td>
          <td>Songwriter</td>
          <td>Actor</td>
        </tr>
      </tbody>
    </table>
"""

component = dmc.RichTextEditor(
    html=table,
    extensions=[
        "StarterKit",
        "Table",
        "TableCell",
        "TableHeader",
        "TableRow",
    ],
)

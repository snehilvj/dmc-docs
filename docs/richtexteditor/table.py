import dash_mantine_components as dmc

table = """
<table>
  <tbody>
    <tr>
      <th><p>Name</p></th>
      <th><p>Role</p></th>
      <th><p>Department</p></th>
    </tr>
    <tr>
      <td><p>Alex Morgan</p></td>
      <td><p>Developer</p></td>
      <td><p>Engineering</p></td>
    </tr>
    <tr>
      <td><p>Jamie Lee</p></td>
      <td><p>Designer</p></td>
      <td><p>Design</p></td>
    </tr>
  </tbody>
</table>
<p></p>
"""

component = dmc.RichTextEditor(
    html=table,
    toolbar={
        "controlsGroups": [
            ["Bold", "Italic", "Underline"],
            ["TableInsert", "TableDelete"],
            ["TableColumnBefore", "TableColumnAfter", "TableColumnDelete"],
            ["TableRowBefore", "TableRowAfter", "TableRowDelete"],
            [
                "TableToggleHeaderRow",
                "TableToggleHeaderColumn",
                "TableMergeCells",
                "TableSplitCell",
            ],
        ],
    },
)
from odoo import fields, models


class MinecraftTellrawLine(models.Model):
    _name = "minecraft.tellraw.line"
    _description = "Minecraft Tellraw Line"
    _order = "sequence,id"

    sequence = fields.Integer(default=1)
    line_break = fields.Boolean()
    text = fields.Char()

    # formatting options
    custom_color = fields.Boolean()
    color = fields.Char()
    bold = fields.Boolean()
    italic = fields.Boolean()
    underlined = fields.Boolean()
    obfuscated = fields.Boolean()
    custom_font = fields.Boolean()
    font = fields.Char(default="minecraft:default")

    # events
    click_event = fields.Selection(
        selection=[
            ("none", "None"),
            ("open_url", "Open URL"),
            ("run_command", "Run command"),
            ("suggest_command", "Suggest Command"),
            ("copy_to_clipboard", "Copy to clipboard"),
        ],
        default="none",
    )
    click_event_text = fields.Char()

    hover_event = fields.Selection(
        selection=[
            ("none", "None"),
            ("show_entity", "Show Entity"),
            ("show_item", "Show Item"),
            ("show_text", "Show Text"),
        ],
        default="none",
    )
    hover_event_text = fields.Char()
    hover_event_show_text_line_ids = fields.One2many(
        comodel_name="minecraft.tellraw.line",
        inverse_name="minecraft_tellraw_line_id",
    )
    is_hover_event_text = fields.Boolean()
    minecraft_tellraw_line_id = fields.Many2one(comodel_name="minecraft.tellraw.line")

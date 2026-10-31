from datetime import datetime, timezone

import discord

from .steam import Changelog, ModDetails, workshop_url

MAX_NOTE = 1500


def build_update_embed(
    details: ModDetails, changelog: Changelog | None, presets: list[str] | None = None
) -> discord.Embed:
    description = ""
    if changelog:
        note = changelog.text
        if len(note) > MAX_NOTE:
            note = note[: MAX_NOTE - 1].rstrip() + "…"
        description = note
    embed = discord.Embed(
        title=f"Mod updated: {details.title}",
        url=workshop_url(details.id),
        description=description or None,
        colour=discord.Colour.blurple(),
        timestamp=datetime.fromtimestamp(details.time_updated, tz=timezone.utc),
    )
    if presets:
        value = ", ".join(presets)
        embed.add_field(name="Preset" if len(presets) == 1 else "Presets", value=value[:1024], inline=False)
    if details.preview_url:
        embed.set_thumbnail(url=details.preview_url)
    embed.set_footer(text=f"Workshop ID {details.id}")
    return embed


def missing_message(title: str, mod_id: int) -> str:
    return (
        f"⚠️ Workshop item **{title}** ({mod_id}) can no longer be found. It was removed or hidden. "
        "I keep watching it; use `/watch remove` to stop."
    )

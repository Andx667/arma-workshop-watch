from bot.steam import parse_changelog, parse_workshop_id

CHANGELOG_HTML = """
<div class="workshopAnnouncement">
  <div class="headline"><a href="#">12 Mar @ 4:05pm</a></div>
  <p id="123">Fixed the thing.<br>Added another thing.</p>
</div>
<div class="workshopAnnouncement">
  <div class="headline">1 Jan @ 1:00am</div>
  <p>Old entry</p>
</div>
"""


def test_parse_id_variants():
    assert parse_workshop_id("463939057") == 463939057
    assert parse_workshop_id(" 463939057 ") == 463939057
    assert parse_workshop_id("https://steamcommunity.com/sharedfiles/filedetails/?id=463939057") == 463939057
    assert parse_workshop_id("https://steamcommunity.com/workshop/filedetails/?l=german&id=463939057&x=1") == 463939057
    assert parse_workshop_id("steam://url/CommunityFilePage/463939057") == 463939057
    assert parse_workshop_id("hello") is None


def test_parse_changelog_takes_newest_entry():
    result = parse_changelog(CHANGELOG_HTML)
    assert result is not None
    assert result.headline == "12 Mar @ 4:05pm"
    assert result.text == "Fixed the thing.\nAdded another thing."


def test_parse_changelog_unknown_layout():
    assert parse_changelog("<html><body>nothing</body></html>") is None

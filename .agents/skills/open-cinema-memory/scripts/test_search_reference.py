#!/usr/bin/env python3

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("search_reference.py")
SPEC = importlib.util.spec_from_file_location("search_reference", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SearchReferenceTests(unittest.TestCase):
    def test_reference_topic_ranks_above_generic_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            topic = root / "docs/reference/topics/projector.md"
            topic.parent.mkdir(parents=True)
            topic.write_text("# Projector\nLaser projector brightness evidence\n", encoding="utf-8")
            generic = root / "notes.txt"
            generic.write_text("Laser projector brightness evidence\n", encoding="utf-8")

            results = MODULE.search(root, "projector brightness")

            self.assertEqual(results[0].path, "docs/reference/topics/projector.md")

    def test_all_query_terms_are_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.md").write_text("projector only\n", encoding="utf-8")
            (root / "two.md").write_text("projector cooling\n", encoding="utf-8")

            results = MODULE.search(root, "projector cooling")

            self.assertEqual([item.path for item in results], ["two.md"])

    def test_templates_and_internal_metadata_are_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = root / "docs/reference/0000-template.md"
            template.parent.mkdir(parents=True)
            template.write_text("projector cooling\n", encoding="utf-8")
            git_file = root / ".git/config"
            git_file.parent.mkdir()
            git_file.write_text("projector cooling\n", encoding="utf-8")
            skill_file = root / ".agents/skills/example/SKILL.md"
            skill_file.parent.mkdir(parents=True)
            skill_file.write_text("projector cooling\n", encoding="utf-8")

            self.assertEqual(MODULE.search(root, "projector cooling"), [])


if __name__ == "__main__":
    unittest.main()


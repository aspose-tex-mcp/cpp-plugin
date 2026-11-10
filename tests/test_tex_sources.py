"""Regression samples from the official TeX repositories; see fixtures/SOURCES.md."""
import unittest
from test_extraction import ROOT, request, worker

class TeXSourceTests(unittest.TestCase):
    def test_tex_docs(self):
        text = (ROOT / "tests/fixtures/tex-conversion.md").read_text(encoding="utf-8")
        result = worker.handle(request(kind="docs", tail="developer-guide/conversion", raw=text))
        self.assertTrue(result["chunk_records"])
        self.assertEqual(result["normalized_document"]["document"]["canonical_url"], "https://docs.aspose.com/tex/cpp/conversion/")
        self.assertIn("Aspose.TeX", str(result["chunk_records"]))

    def test_texjob_class_and_run(self):
        for filename, tail, fqn in [("texjob", "aspose.tex/texjob", "Aspose.TeX.TeXJob"), ("texjob-run", "aspose.tex/texjob/run", "Aspose.TeX.TeXJob.Run")]:
            with self.subTest(filename=filename):
                text = (ROOT / f"tests/fixtures/{filename}.md").read_text(encoding="utf-8")
                result = worker.handle(request(kind="apiref", tail=tail, raw=text))
                self.assertTrue(result["symbols"])
                symbol = result["symbols"][0]
                self.assertEqual(symbol["member_fqn"], fqn)
                self.assertTrue(symbol["signature"])
                self.assertIn("/tex/cpp/aspose.tex/texjob/", symbol["canonical_url"])
                self.assertEqual(symbol["language"], "cpp")
                if filename == "texjob-run":
                    self.assertEqual(symbol["signature"], "Aspose::TeX::TeXJobResult Aspose::TeX::TeXJob::Run()")

#!/usr/bin/env python3
from . import PageLabelScheme
from pdfrw import PdfName, PdfDict, PdfArray

class PageLabels(list):
    @classmethod
    def from_pdf(cls, pdf):
        labels = pdf.Root.PageLabels
        if not labels: return cls([])
        nums = labels.Nums
        parsed = (PageLabelScheme.from_pdf(nums[i], nums[i+1])
                    for i in range(0, len(nums), 2))
        return cls(parsed)

    def normalize(self, pagenum=float("inf")):
        """Sort the pagelabels, remove duplicate entries,
        and if pegenum is set remove entries that have a startpage >= pagenum"""
        self.sort()
        if len(self) == 0 or self[0].startpage != 0:
            self.insert(0, PageLabelScheme(0))
        # Remove duplicates
        pagenums = set()
        for elem in self[:]:
            if elem.startpage in pagenums or elem.startpage >= pagenum:
                self.remove(elem)
            else:
                pagenums.add(elem.startpage)

    def pdfdict(self):
        """Return a PageLabel entry to pe inserted in the root of a PdfReader object"""
        nums = (i for label in sorted(self)
                    for i in label.pdfobjs())
        return PdfDict(Type=PdfName("Catalog"),
                       Nums = PdfArray(nums))

    def write_raw(self, pdf):
        """Write the PageLabels to a PdfReader object without sanity checks
        Use at your own risks, this may corrupt your PDF"""
        pdf.Root.PageLabels = self.pdfdict()

    def write(self, pdf):
        """Write the PageLabels to a PdfReader object, normalizing it first"""
        self.normalize(len(pdf.pages))
        pdf.Root.PageLabels = self.pdfdict()

# pagelabels python library

This is a little library, based on **pdfrw**, that helps manipulate PDF page labels in python.
It can parse page labels from  a PDF, edit page labels, and write them in a PDF.

For more info about page labels, see: https://www.w3.org/TR/WCAG20-TECHS/PDF17.html

## Classes

### PageLabels
Inherits from list and represents a list of `PageLabelScheme`s.

### PageLabels.from_pdf(pdfrwobj)
Static method.
Read page labels from a PdfReader object.

### .write(pdfrwobj)
Write the page labels to a PdfReader object.

### PageLabelScheme
Inherits from a named tuple with fields:
 * `startpage` : Index in the PDF where to start numbering pages according to this scheme
 * `style` : one of the strings `arabic`, `roman uppercase`, `letters uppercase`, `roman lowercase`, `letters lowercase`
 * `prefix` : string to prepend to all page labels
 * `firstpagenum` : where to start the index

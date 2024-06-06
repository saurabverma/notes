## Merge several pdf

```bash
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dAutoRotatePages=/None -sOutputFile=finished.pdf  file1.pdf file2.pdf
```

## Crop a pdf

```bash
gs -o cropped.pdf -sDEVICE=pdfwrite -c "[/CropBox [48 72 547 722]" -c " /PAGES pdfmark" -f uncropped-input.pdf
```

NOTE: The measurement unit for PDF is the same as for PostScript: it's called a point `pt`.

```
72 pt == 1" == 25.4 mm
```
Typically, A4 size is
```
width: 595 pt == 210 mm
height: 842 pt == 297 mm
```
Then, assuming we want to crop off
```
   left edge: 48 pt == 2/3" ~= 16.9 mm
 bottom edge: 72 pt ==   1" ~= 25.4 mm
  right edge: 48 pt == 2/3" ~= 16.9 mm
    top edge: 120 pt == 5/3" ~= 42.3 mm
```
the `CropBox` dimensions become
```
[48 72 595-48 842-120] == [48 72 547 722]
```

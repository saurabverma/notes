## Merge several pdf

```bash
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dAutoRotatePages=/None -sOutputFile=finished.pdf  file1.pdf file2.pdf
```

## Crop a pdf

```bash
gs -o cropped.pdf -sDEVICE=pdfwrite -c "[/CropBox [24 72 559 794]" -c " /PAGES pdfmark" -f uncropped-input.pdf
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
   left edge: 24 pt == 1/3" ~=  8.5 mm
 bottom edge: 72 pt ==   1" ~= 25.4 mm
  right edge: 36 pt == 1/2" ~= 12.7 mm
    top edge: 48 pt == 2/3" ~= 17.0 mm
```
the `CropBox` dimensions become
```
[24 72 595-36 842-48] == [24 72 559 794]
```

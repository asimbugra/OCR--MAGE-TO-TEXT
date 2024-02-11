# OCR--MAGE-TO-TEXT

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OCR ile Metin Tanıma</title>
</head>
<body>

<h1>OCR ile Metin Tanıma</h1>

<p>Bu proje, Tesseract OCR kütüphanesi kullanılarak resimlerdeki metni tanıma amacıyla geliştirilmiştir.</p>

<h2>Kurulum</h2>

<p>Öncelikle, gerekli Python kütüphanelerini yüklemek için aşağıdaki komutları kullanabilirsiniz:</p>

<pre>
pip install Pillow
pip install pytesseract
</pre>

<p>Ayrıca, Tesseract OCR'ı <a href="https://github.com/tesseract-ocr/tesseract">resmi web sitesinden</a> indirip kurmanız gerekmektedir.</p>

<h2>Kullanım</h2>

<h3>Latin Alfabesi İçin OCR</h3>

<p><code>latin_ocr.py</code> dosyası, sadece Latin alfabesi içeren metinleri tanıma amacıyla kullanılır. Örnek kullanım:</p>

<pre>
python latin_ocr.py /path/to/image.png
</pre>

<h3>Diğer Alfabeleri Tanıma İçin OCR</h3>

<p><code>multi_language_ocr.py</code> dosyası, çoklu dilleri destekleyen OCR tanıma amacıyla kullanılır. Örnek kullanım:</p>

<pre>
python multi_language_ocr.py /path/to/image.png
</pre>

<p>Dil belirtilmeden genel bir tanıma yapmak için:</p>

<pre>
python multi_language_ocr.py /path/to/image.png
</pre>

<h3>Notlar</h3>

<ul>
    <li>Resminiz yolu <code>/path/to/image.png</code> ile değiştirilmelidir.</li>
    <li>Tesseract OCR'ın doğru bir şekilde çalışabilmesi için Tesseract OCR'ın yüklü olduğundan emin olun.</li>
</ul>

</body>
</html>

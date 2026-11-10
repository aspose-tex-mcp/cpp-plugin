---
title: Aspose::TeX::FileCorruptedException typedef
linktitle: FileCorruptedException
second_title: Aspose.TeX for C++ API Reference
description: 'Aspose::TeX::FileCorruptedException typedef. Thrown during document load, when the document appears to be corrupted and impossible to load. To learn more, visit the  documentation article in C++.'
type: docs
weight: 133000
url: /cpp/aspose.tex/filecorruptedexception/
---
## FileCorruptedException typedef


Thrown during document load, when the document appears to be corrupted and impossible to load. To learn more, visit the [Programming with Documents](https://docs.aspose.com/tex/cpp/programming-with-documents/) documentation article.

```cpp
using Aspose::TeX::FileCorruptedException = typedef System::ExceptionWrapper<Details_FileCorruptedException>
```


## Examples



Shows how to catch a FileCorruptedException. 
```cpp
try
{
    // If we get an "Unreadable content" error message when trying to open a document using Microsoft Word,
    // chances are that we will get an exception thrown when trying to load that document using Aspose.TeX.
    auto doc = System::MakeObject<Aspose::TeX::Document>(System::String(get_MyDir() + u"Corrupted document.docx"));
}
catch (Aspose::TeX::FileCorruptedException& e)
{
    std::cout << e->get_Message() << std::endl;
}
```

## See Also

* Namespace [Aspose::TeX](../)
* Library [Aspose.TeX for C++](../../)

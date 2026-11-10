---
title: Aspose::TeX::IDocumentReaderPlugin interface
linktitle: IDocumentReaderPlugin
second_title: Aspose.TeX for C++ API Reference
description: 'Aspose::TeX::IDocumentReaderPlugin interface. Defines an interface for external reader plugins that can read a file into a document in C++.'
type: docs
weight: 77000
url: /cpp/aspose.tex/idocumentreaderplugin/
---
## IDocumentReaderPlugin interface


Defines an interface for external reader plugins that can read a file into a document.

```cpp
class IDocumentReaderPlugin : public virtual System::Object
```

## Methods

| Method | Description |
| --- | --- |
| [GetType](./gettype/)() const override |  |
| [Is](./is/)(const System::TypeInfo\&) const override |  |
| virtual [Read](./read/)(System::SharedPtr\<System::IO::Stream\>, System::SharedPtr\<Aspose::TeX::Loading::LoadOptions\>, System::SharedPtr\<Aspose::TeX::Document\>) | Reads the data from the specified stream into the [Document](../document/) instance. |
| static [Type](./type/)() |  |
## See Also

* Namespace [Aspose::TeX](../)
* Library [Aspose.TeX for C++](../../)

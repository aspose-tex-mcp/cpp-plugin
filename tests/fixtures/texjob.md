---
title: Aspose::TeX::TeXJob class
linktitle: TeXJob
second_title: Aspose.TeX for C++
description: 'Aspose::TeX::TeXJob class. Implements features of a TeX job in C++.'
type: docs
weight: 700
url: /cpp/aspose.tex/texjob/
---
## TeXJob class


Implements features of a [TeX](../) job.

```cpp
class TeXJob : public System::Object
```

## Methods

| Method | Description |
| --- | --- |
| static [CreateFormat](./createformat/)(const System::String\&, const System::SharedPtr\<Aspose::TeX::TeXOptions\>\&) | Runs [TeX](../) engine in INITEX mode to create a format file (.fmt). |
| [Run](./run/)() | Runs [TeX](../) job. |
| [TeXJob](./texjob/)(const System::SharedPtr\<System::IO::Stream\>\&, const System::SharedPtr\<Aspose::TeX::Presentation::Device\>\&, const System::SharedPtr\<Aspose::TeX::TeXOptions\>\&) | Creates a [TeX](../) job for running the engine in production mode to typeset a [TeX](../) file. |
| [TeXJob](./texjob/)(const System::String\&, const System::SharedPtr\<Aspose::TeX::Presentation::Device\>\&, const System::SharedPtr\<Aspose::TeX::TeXOptions\>\&) | Creates a [TeX](../) job for running the engine in production mode to typeset a [TeX](../) file. |
| [TeXJob](./texjob/)(const System::SharedPtr\<Aspose::TeX::Presentation::Device\>\&, const System::SharedPtr\<Aspose::TeX::TeXOptions\>\&) | Creates a [TeX](../) job for running the engine in production mode to typeset a [TeX](../) document. The engine will prompt the file name as soon as it starts. Thus this run is supposed to be interactive. |
## See Also

* Class [Object](../../system/object/)
* Namespace [Aspose::TeX](../)
* Library [Aspose.TeX for C++](../../)

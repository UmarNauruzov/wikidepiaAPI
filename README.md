# wikidepiaAPI

# Входные данные: 
* 1) 2 ссылки на wikipedia (можно из файла можно из консоли вводить)
* 2) ссылки за пределами wikipedia путем не считаются
* 3) вручную от одной страницы до второй можно дойти за 3 клика (см прмиер)
* 4) необходимо показать полный путь как пройти от ссылки 1 до ссылки 2. 
* 5) отображение пути должно для каждого шага должно содержать текст (полное предложение в котором эта ссылка найдена) и ссылку на следующую страницу
* 6) отображать это можно как в консоли так и в web
* 7) дополнительно можно вести лог файл со всеми страницами что были посещены при поиске

Исходные ссылки: стартовая - https://ru.wikipedia.org/wiki/Xbox_360_S

Конечная - https://ru.wikipedia.org/wiki/Nintendo_3DS

## Решение

Мною был выбран скрипт для краулинга (парсинга) Википедии, который ищет путь от одной статьи Википедии до другой. Код написан на языке Python и использует библиотеки requests и BeautifulSoup для получения и обработки HTML-кода страницы Википедии.

Класс WikipediaCrawler содержит метод crawl, который принимает два параметра: начальную и конечную ссылки на страницы Википедии. Метод crawl добавляет начальную ссылку в множество ссылок, которые нужно посетить, и вызывает метод _bfs, который осуществляет поиск в ширину на страницах Википедии, начиная с начальной ссылки, и возвращает кратчайший путь (если он существует) от начальной ссылки до конечной ссылки.

Метод _bfs использует очередь для поиска в ширину. Каждый раз, когда элемент извлекается из очереди, он посещается, и его содержимое (HTML-код) парсится с помощью BeautifulSoup. Все ссылки, найденные на этой странице, проверяются на предмет того, что они ведут на страницу Википедии, и если это так, то они добавляются в очередь, если их еще нет в множестве уже посещенных страниц.

Если краулер находит конечную ссылку, он возвращает кратчайший путь, состоящий из последовательности ссылок, начиная с начальной ссылки и заканчивая конечной ссылкой. Если кратчайший путь не существует, возвращается пустой список.

Если кратчайший путь найден, скрипт выводит текст первого абзаца для каждой страницы в пути, а также ссылку на следующую страницу в пути (если она есть). Если путь не найден он выводит соответствующее сообщение.

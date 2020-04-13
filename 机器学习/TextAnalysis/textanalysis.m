clear;
clc;
%% 导入文档
my_str = extractFileText("Pride and Prejudice.txt");
%% 查看
extractBefore(my_str,269)
i = strfind(my_str,"I");
ii = strfind(my_str,"II");
start = ii(1);
fin = ii(2);
extractBetween(my_str,start,fin-1)

%% 词云
T = wordCloudCounts(my_str);
figure('Name','First','NumberTitle','off');
subplot(2,1,1);
wordcloud(my_str);
subplot(2,1,2);
wordcloud(T.Word, T.Count);
%% 分词
s = eraseURLs(my_str);
s = eraseTags(s);
% s = decodeHTMLEntities(s);
s = lower(s);
s = erasePunctuation(s);
doc = tokenizedDocument(s);
size(doc.Vocabulary)
clean_doc = removeWords(doc, stopWords);
bag = bagOfWords(clean_doc);
topkwords(bag, 20)
figure('Name','Second','NumberTitle','off');
wordcloud(bag);



%% 一次读取多个文档
% fds = fileDatastore('exampleSonnet*.txt','ReadFcn',@extractFileText)

%% 正则表达式
contacts = { ...
'Harry  287-625-7315  Columbus, OH  hparker@hmail.com'; ...
'Janice  529-882-1759  Fresno, CA  jan_stephens@horizon.net'; ...
'Mike  793-136-0975  Richmond, VA  sue_and_mike@hmail.net'; ...
'Nadine  648-427-9947  Tampa, FL  nadine_berry@horizon.net'; ...
'Jason  697-336-7728  Montrose, CO  jason_blake@mymail.com'};
% contains, strfind
% startsWith, endsWith
% repalce
% extractAfter, extractBetween
% regexp, regexpi, regexprep

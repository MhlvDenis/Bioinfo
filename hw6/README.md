# Отчет

## Часть первая

### 1)
[Директория](proteins): в каждой папке .fasta файл с белком человека и его ортологом у шимпанзе, их выравнивание и скрин с identities и similarity (positives)  
Сводная таблица:  
| Human Protein | Pan Troglodytes Protein | Identity | Similarity |
|---------------|-------------------------|----------|------------|
| ECD_HUMAN     | A0A2I3RSG0_PANTR        | 99%      | 99%        |
| BRCA1_HUMAN   | BRCA1_PANTR             | 98%      | 98%        |
| TPMT_HUMAN    | TPMT_PANTR              | 99%      | 99%        |
| APOE_HUMAN    | APOE_PANTR              | 97%      | 98%        |
| ACTB_HUMAN    | ACTB_PANTR              | 100%     | 100%       |
| HELZ_HUMAN    | H2QDQ4_PANTR            | 99%      | 99%        |
| PML_HUMAN     | H2Q9S3_PANTR            | 91%      | 91%        |
| HBB_HUMAN     | HBB_PANTR               | 100%     | 100%       |
| HSPB1_HUMAN   | H2QUT1_PANTR            | 100%     | 100%       |
| MYH7_HUMAN    | A0A2I3SXF0_PANTR        | 99%      | 99%        | 

Среднее identity: 98.2%  
Среднее similarity: 98.3%

### 3)

## Часть вторая
### 1)
#### Вопрос 0:
![](psr.png)  
#### Вопрос 1 + 2:
Загружаем [30.fasta](30.fasta) в BLAST, для каждого рида смотрим лучший матч, у которого identity >= 99%. Для таких видов записываем description, в котором указан вид. [Результат](reads.txt).  
В чтениях присутствуют виды:
| Вид                    | Доля |
|------------------------|------|
| Canis lupus familiaris | 26%  |
| Homo sapiens           | 13%  |
| Lutra lutra            | 1%   |
| Mus musculus           | 47%  |
| NaN                    | 13%  |  

Таким образом виновник загрязнения Иванов, т.к. есть процент загрязнения от Canis lupus familiaris, и нет ни одного рида, классифицированного как Felis catus.  
По доле каждого вида, можно сделать вывод, что есть загрязнение от собаки и человека. Выдра (Lutra lutra) это, вероятно, выброс.

### 2)

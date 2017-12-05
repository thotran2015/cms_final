// Housing data from https://archive.ics.uci.edu/ml/datasets/Housing
window.HOUSING_DATA=[{coords: [ 0.00632,  18.00,   2.310], tags: ['Friends','Family']},
{coords: [ 8.32,  12.00,   13.10], tags: ['Friends','Exams']},
{coords: [ 2.832,  16.00,   13.10], tags: ['Exams']},
{coords: [ 1.832,  14.00,   33.10], tags: ['Coursework']},
{coords: [ 8.32,  12.00,   25.10], tags: ['Family','Employment']}];

{% for sub in submissions %}
  var submit = {coords: [ {{sub.happy}},  {{sub.excited}},   2.310], tags: ['Friends','Family']}
  window.HOUSING_DATA.push(submit)

{% endfor %}

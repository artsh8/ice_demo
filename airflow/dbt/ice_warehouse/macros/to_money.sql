{% macro to_money(column_name) %}
    CAST(({{ column_name }} * 0.01) AS DECIMAL(19,2))
{% endmacro %}

SELECT DISTINCT
    -- Generate a random 6-digit number for Surrogate_Person_ID
    CAST(FLOOR(RAND() * 900000) + 100000 AS INTEGER) AS Surrogate_Person_ID,
    
    -- Extract the Salutation (e.g., Mr., Ms., Dr.) from the Name field
    CASE
        WHEN SPLIT(TRIM(Name), ' ')[0] IN ('Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Prof.') THEN SPLIT(TRIM(Name), ' ')[0]
        ELSE NULL
    END AS Salutation,
    
    -- Extract Suffix (e.g., Jr., Sr., II) from the Name field, if present
    CASE
        WHEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1] IN ('Jr.', 'Sr.', 'II', 'III', 'IV') THEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1]
        ELSE NULL
    END AS Suffix,
    
    -- Extract Title (e.g., PhD, MBA, DVM) from the Name field, if present
    CASE
        WHEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1] IN ('PhD', 'MBA', 'Esq.', 'MD', 'DDS', 'DO', 'JD', 'DVM') THEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1]
        ELSE NULL
    END AS Title,
    
    -- Extract First_Name from the Name field, considering if a salutation is present
    CASE
        WHEN SPLIT(TRIM(Name), ' ')[0] IN ('Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Prof.') THEN SPLIT(TRIM(Name), ' ')[1]
        ELSE SPLIT(TRIM(Name), ' ')[0]
    END AS First_Name,
    
    -- Extract Surname from the Name field, considering suffixes and titles
    CASE
        WHEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1] IN ('PhD', 'MBA', 'Esq.', 'MD', 'DDS', 'DO', 'JD', 'DVM') THEN
            SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 2]
        WHEN SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1] IN ('Jr.', 'Sr.', 'II', 'III', 'IV') THEN
            SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 2]
        ELSE
            SPLIT(TRIM(Name), ' ')[SIZE(SPLIT(TRIM(Name), ' ')) - 1]
    END AS Surname,
    
    -- Format Phone_Number based on presence of an extension (x)
    CASE
        WHEN INSTR(Phone_Number, 'x') > 0 THEN
            CASE 
                WHEN Phone_Number LIKE '+1%' THEN
                    CONCAT('+1 ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3, INSTR(Phone_Number, 'x') - 3), '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3, INSTR(Phone_Number, 'x') - 3), '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3, INSTR(Phone_Number, 'x') - 3), '[^0-9]', ''), 7, 4))
                WHEN Phone_Number LIKE '001%' THEN
                    CONCAT('+1 ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4, INSTR(Phone_Number, 'x') - 4), '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4, INSTR(Phone_Number, 'x') - 4), '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4, INSTR(Phone_Number, 'x') - 4), '[^0-9]', ''), 7, 4))
                ELSE
                    CONCAT(
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 1, INSTR(Phone_Number, 'x') - 1), '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 1, INSTR(Phone_Number, 'x') - 1), '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 1, INSTR(Phone_Number, 'x') - 1), '[^0-9]', ''), 7, 4))
            END
        ELSE
            CASE 
                WHEN Phone_Number LIKE '+1%' THEN
                    CONCAT('+1 ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3), '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3), '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 3), '[^0-9]', ''), 7, 4))
                WHEN Phone_Number LIKE '001%' THEN
                    CONCAT('+1 ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4), '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4), '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(SUBSTRING(Phone_Number, 4), '[^0-9]', ''), 7, 4))
                ELSE
                    CONCAT(
                        SUBSTRING(REGEXP_REPLACE(Phone_Number, '[^0-9]', ''), 1, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(Phone_Number, '[^0-9]', ''), 4, 3),
                        ' ',
                        SUBSTRING(REGEXP_REPLACE(Phone_Number, '[^0-9]', ''), 7, 4))
            END
    END AS Phone_Number,
    
    -- Extract Phone_Extension number if present
    CASE
        WHEN INSTR(Phone_Number, 'x') > 0 THEN
            REGEXP_REPLACE(SUBSTRING(Phone_Number, INSTR(Phone_Number, 'x') + 1), '[^0-9]', '')
        ELSE NULL
    END AS Phone_Extension,
    
    -- Convert email addresses to lower case
    LOWER(Email) AS Email,
    
    -- Capitalise Job_Titles and replace 'And' with 'and'
    REGEXP_REPLACE(INITCAP(Title), '\\bAnd\\b', 'and') AS Job_Title,
    
    -- Generate a consistent surrogate ID for each company based on Company_Name
    CONCAT(
        SUBSTRING(
            UPPER(
                CONV(
                    SUBSTRING(
                        SHA2(UPPER(TRIM(Company)), 256),
                        1,
                        12
                    ),
                    16,
                    36
                )
            ),
            1,
            6
        )
    ) AS Surrogate_Company_ID,

    -- Extract the Company_Name without legal structures
    CASE
        WHEN Company IS NOT NULL THEN 
            TRIM(REGEXP_REPLACE(
                TRIM(Company),
                '(?i)\\b(LLC|Ltd|PLC|Inc|Corp|LLP|PTY|GmbH|AG)\\b.*$', ''
            ))
        ELSE NULL
    END AS Company_Name,
    
    -- Extract the Business_Structure (e.g., LLC, Ltd, PLC) from the company name
    CASE
        WHEN Company IS NOT NULL THEN 
            REGEXP_EXTRACT(Company, '(?i)(LLC|Ltd|PLC|Inc|Corp|LLP|PTY|GmbH|AG)\\b')
        ELSE NULL
    END AS Business_Structure
FROM crm_test_case_data_People;

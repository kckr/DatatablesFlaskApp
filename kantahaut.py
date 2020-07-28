import pyodbc


class LaatuSearch:
    def __init__(self):
        self.conn_str = "Driver={ODBC Driver 13 for SQL Server};Server=*****;Database=****;Trusted_Connection=yes;'"
        self.cnxn = pyodbc.connect(self.conn_str)
        self.cursor = self.cnxn.cursor()

    def table_all_ecos(self):

        eco_name = []
        eco_originator = []
        production_line = []
        eco_released = []
        eco_originated = []
        eco_lahetyspaiva = []
        eco_imp_in_prod = []
        eco_verified = []
        eco_description = []

        eco_category_of_change = []
        eco_level = []
        tracking_comment = []

        aaa = """SELECT tulokset.[ECO_Name], Enumerot.Nimi,  [Linja], tulokset.[ECO_Released], tulokset.ECO_Originated, coalesce(pv.[Supplier_sent_date], '1999-01-01') as lahetyspaiva,  tulokset.ECO_Impl_in_production, tulokset.ECO_Impl_verified_date, 
            tulokset.[ECO_Description],ECO_Oracle_Status.OracleStatus, ECO_Level.LevelName, ECO_ECR_Categories.ECO_ECR_Category, Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Linjat] inner join (SELECT  ECO_Uudet_Ecot.[ECO_Name],ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 1 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L1='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name],ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description] ,ECO_Uudet_Ecot.[ECO_Released]
              ,ECO_Uudet_Ecot.[Oracle_Status] ,ECO_Uudet_Ecot.[ECO_level] , 2 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L2='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 3 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L3='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 4 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L4='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level] , 5 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L5='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 6 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L6='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name],ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released]  ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level] ,7 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L7='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 8 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L8='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name],ECO_Uudet_Ecot.[ECO_Originator],ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level] , 9 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L9='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released] ,ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 10 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L10='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name],ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 11 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L11='True' union
        
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 12 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L12='True' union
            
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 13 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L13='True' union
            
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 14 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L14='True' union
            
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 15 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L15='True' union
            
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 16 as LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] =[ECO_Ecot_linjoittain].[Eco_Name]
            where L16='True' union
            
            
            SELECT  ECO_Uudet_Ecot.[ECO_Name] ,ECO_Uudet_Ecot.[ECO_Originator] ,ECO_Uudet_Ecot.[ECO_Description]
              ,ECO_Uudet_Ecot.[ECO_Released],ECO_Uudet_Ecot.[Oracle_Status]
              ,ECO_Uudet_Ecot.[ECO_level], 19  LinjaID, ECO_Uudet_Ecot.ECO_Originated, ECO_Uudet_Ecot.ECO_Impl_in_production, ECO_Uudet_Ecot.ECO_Impl_verified_date, ECO_Uudet_Ecot.ECO_Category_of_change, ECO_Uudet_Ecot.Tracking_comment
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] left Join [ECO_Ecot_linjoittain] on ECO_Uudet_Ecot.[ECO_Name] = [ECO_Ecot_linjoittain].[Eco_Name]
            where  [ECO_Ecot_linjoittain].[ECO_Name] is NULL
            
            
        
            )  tulokset on LinjaID = ID left join [ECO_Oracle_Status] on tulokset.[Oracle_Status] =[OracleStatusID] left join [ECO_Level] on tulokset.ECO_level = [ECO_Level].LevelID left join (select * from ECO_Supplier_Junction where
            [Supplier_sent_date] in (Select max([Supplier_sent_date]) FROM ECO_Supplier_Junction group by [ECO_name])) as pv on tulokset.ECO_Name = pv.ECO_name left join Enumerot on tulokset.[ECO_Originator] = Enumerot.ENUMERO left join [ECO_ECR_Categories] on tulokset.ECO_Category_of_change = ECO_ECR_Categories.CategoryID
            
            """

        rows = self.cursor.execute(aaa).fetchall()
        for row in rows:

            muuttuja = row.ECO_Name
            if muuttuja is None:
                muuttuja = ""
                eco_name.append(muuttuja)
            else:
                eco_name.append(muuttuja)

            muuttuja = row.Nimi  # ECO-originators name to lista2
            if muuttuja is None:
                muuttuja = "External User"
                eco_originator.append(muuttuja)

            else:
                eco_originator.append(muuttuja)

            muuttuja = row.Linja
            if muuttuja is None:
                muuttuja = ""
                production_line.append(muuttuja)
            else:
                production_line.append(muuttuja)

            muuttuja = row.ECO_Released
            if muuttuja is None:
                muuttuja = ""
                eco_released.append(muuttuja)
            else:
                eco_released.append(muuttuja)

            muuttuja = row.ECO_Originated
            if muuttuja is None:
                muuttuja = ""
                eco_originated.append(muuttuja)
            else:
                eco_originated.append(muuttuja)

            muuttuja = row.lahetyspaiva
            if muuttuja is None:
                muuttuja = ""
                eco_lahetyspaiva.append(muuttuja)
            else:
                eco_lahetyspaiva.append(muuttuja)

            muuttuja = row.ECO_Impl_in_production
            if muuttuja is None:
                muuttuja = ""
                eco_imp_in_prod.append(muuttuja)
            else:
                eco_imp_in_prod.append(muuttuja)

            muuttuja = row.ECO_Impl_verified_date
            if muuttuja is None:
                muuttuja = ""
                eco_verified.append(muuttuja)
            else:
                eco_verified.append(muuttuja)

            muuttuja = row.ECO_Description
            if muuttuja is None:
                muuttuja = ""
                eco_description.append(muuttuja)
            else:
                eco_description.append(muuttuja)

            muuttuja = row.ECO_ECR_Category
            if muuttuja is None:
                muuttuja = ""
                eco_category_of_change.append(muuttuja)
            else:
                eco_category_of_change.append(muuttuja)

            muuttuja = row.LevelName
            if muuttuja is None:
                muuttuja = ""
                eco_level.append(muuttuja)
            else:
                eco_level.append(muuttuja)

            muuttuja = row.Tracking_comment
            if muuttuja is None:
                muuttuja = ""
                tracking_comment.append(muuttuja)
            else:
                tracking_comment.append(muuttuja)

        self.cnxn.commit()
        zip_list = zip(eco_name, eco_originator, production_line, eco_released, eco_originated,
                       eco_category_of_change, eco_level, eco_imp_in_prod, eco_verified, tracking_comment,
                       eco_description)
        # diceco_list = dict((z[0], list(z[1:])) for z in zip(listatable4, list2, list3))
        # eco_table1 = list(dict.fromkeys(zip_list))
        eco_table1 = list(zip_list)

        return eco_table1

    def ecos_by_suppliers(self):

        eco_name_t2 = []
        eco_originator_t2 = []
        supplier_name = []
        supplier_sent_date = []
        date_eco_received = []
        date_satus_confirmed = []
        eco_imp_in_prod_t2 = []
        supplier_comments = []

        # noinspection SqlResolve
        ccc = """SELECT [ECO_Supplier_Junction].[ECO_name]
            ,Enumerot.Nimi
            ,[ECO_Suppliers].[Supplier_Name]
            ,[ECO_Supplier_Junction].[Supplier_sent_date]
            ,[ECO_Supplier_Junction].[Date_ECO_received]
            ,[ECO_Supplier_Junction].[Status_Confirmed_date]
            ,[ECO_Uudet_Ecot].[ECO_Impl_in_production]
            ,[ECO_Supplier_Junction].[Supplier_Comments]
    
            FROM [Laatu2].[dbo].[ECO_Supplier_Junction] join ECO_Uudet_Ecot on ECO_Supplier_Junction.ECO_name = ECO_Uudet_Ecot.ECO_Name 
            join Enumerot on ECO_Uudet_Ecot.ECO_Originator = Enumerot.ENUMERO join ECO_Suppliers on ECO_Supplier_Junction.Supplier_ID = ECO_Suppliers.Supplier_ID
            order by [ECO_Supplier_Junction].[ECO_name]"""

        rows = self.cursor.execute(ccc).fetchall()
        for row in rows:

            muuttuja = row.ECO_name
            if muuttuja is None:
                muuttuja = ""
                eco_name_t2.append(muuttuja)
            else:
                eco_name_t2.append(muuttuja)

            muuttuja = row.Nimi  # ECO Originator
            if muuttuja is None:
                muuttuja = "External User"
                eco_originator_t2.append(muuttuja)
            else:
                eco_originator_t2.append(muuttuja)

            muuttuja = row.Supplier_Name
            if muuttuja is None:
                muuttuja = ""
                supplier_name.append(muuttuja)
            else:
                supplier_name.append(muuttuja)

            muuttuja = row.Supplier_sent_date
            if muuttuja is None:
                muuttuja = ""
                supplier_sent_date.append(muuttuja)
            else:
                supplier_sent_date.append(muuttuja)

            muuttuja = row.Date_ECO_received
            if muuttuja is None:
                muuttuja = ""
                date_eco_received.append(muuttuja)
            else:
                date_eco_received.append(muuttuja)

            muuttuja = row.Status_Confirmed_date
            if muuttuja is None:
                muuttuja = ""
                date_satus_confirmed.append(muuttuja)
            else:
                date_satus_confirmed.append(muuttuja)

            muuttuja = row.ECO_Impl_in_production
            if muuttuja is None:
                muuttuja = ""
                eco_imp_in_prod_t2.append(muuttuja)
            else:
                eco_imp_in_prod_t2.append(muuttuja)

            muuttuja = row.Supplier_Comments
            if muuttuja is None:
                muuttuja = ""
                supplier_comments.append(muuttuja)
            else:
                supplier_comments.append(muuttuja)

            self.cnxn.commit()

        zip_list2 = zip(eco_name_t2, eco_originator_t2, supplier_name, supplier_sent_date, date_eco_received,
                        date_satus_confirmed, eco_imp_in_prod_t2, supplier_comments)
        eco_table2 = list(zip_list2)
        return eco_table2

    def table_suppliers_n_items(self):
        # ECO Information - ECOs by suppliers

        lista33 = []
        lista34 = []
        lista35 = []
        lista36 = []
        lista37 = []
        lista38 = []
        listaqty_3 = []

        bbb = """SELECT DISTINCT 
            [ECO_Item_Junction].[ECO_name]
            ,[ECO_Item_Junction].[Supplier_ID]
            ,[ECO_Item_Junction].[Item_Name]
            ,[ECO_Item_Junction].[Item_New_rev]
            ,[ECO_Item_Junction].[New_Price]
            ,[ECO_Item_Junction].[Old_revision_qty]
    
            ,[ECO_Uudet_Osat].[Item_Name] as ItemName
            ,[ECO_Uudet_Osat].[Item_Description] as ItemDescription
            ,[ECO_Uudet_Osat].[Item_New_rev] as NewRev
    
            ,[ECO_Suppliers].[Supplier_ID]
            ,[ECO_Suppliers].[Supplier_Name]
    
            FROM [Laatu2].[dbo].[ECO_Item_Junction] join [ECO_Uudet_Osat] on ECO_Item_Junction.Item_Name = ECO_Uudet_Osat.Item_Name and ECO_Item_Junction.Item_New_rev = ECO_Uudet_Osat.Item_New_rev
            join ECO_Suppliers on ECO_Item_Junction.Supplier_ID = ECO_Suppliers.Supplier_ID 
            order by [ECO_Item_Junction].[ECO_name]"""

        rows = self.cursor.execute(bbb).fetchall()
        for row in rows:

            muuttuja = row.ECO_name
            if muuttuja is None:
                muuttuja = ""
                lista33.append(muuttuja)
            else:
                lista33.append(muuttuja)

            muuttuja = row.Supplier_Name
            if muuttuja is None:
                muuttuja = ""
                lista34.append(muuttuja)
            else:
                lista34.append(muuttuja)

            muuttuja = row.ItemName
            if muuttuja is None:
                muuttuja = ""
                lista35.append(muuttuja)
            else:
                lista35.append(muuttuja)

            muuttuja = row.ItemDescription
            if muuttuja is None:
                muuttuja = ""
                lista36.append(muuttuja)
            else:
                lista36.append(muuttuja)

            muuttuja = row.NewRev
            if muuttuja is None:
                muuttuja = ""
                lista37.append(muuttuja)
            else:
                lista37.append(muuttuja)

            muuttuja = row.New_Price
            if muuttuja is None:
                muuttuja = ""
                lista38.append(muuttuja)
            else:
                lista38.append(muuttuja)

            muuttuja = row.Old_revision_qty
            if muuttuja is None:
                muuttuja = ""
                listaqty_3.append(muuttuja)
            else:
                listaqty_3.append(muuttuja)
        self.cnxn.commit()
        zip_list3 = zip(lista33, lista34, lista35, lista36, lista37, lista38, listaqty_3)
        eco_table3 = list(zip_list3)  # converting zip list for iteration
        return eco_table3


    def table_items(self):

        lista10 = []
        lista11 = []
        lista12 = []
        lista13 = []
        lista14 = []
        lista15 = []
        lista16 = []
        lista17 = []
        lista18 = []
        lista19 = []
        lista20 = []
        lista21 = []
        lista22 = []
        listaqty = []
        originator_list = []
        originator_list_name = []

        ddd = """SELECT DISTINCT 
            [ECO_Uudet_Ecot].[ECO_Name]
    
            ,[ECO_Uudet_Ecot].[ECO_Impl_in_production]
            ,[ECO_Uudet_Ecot].[ECO_Impl_in_production_NN]
            ,[ECO_Uudet_Ecot].[ECO_Impl_verified_NN]
            ,[ECO_Uudet_Ecot].[ECO_Impl_verified_date]
            ,[ECO_Uudet_Ecot].[ECO_Impl_verified_kommentti]
            ,[ECO_Uudet_Ecot].[ECO_Originator]
            ,[Enumerot].[Nimi]
    
            ,coalesce(a.InProcessName,'') as Prosessissa
            ,coalesce(b.InProcessName,'') as Orderissa
            ,coalesce(c.InProcessName,'') as Stockissa
            ,coalesce(d.InProcessName,'') as Fieldilta
            ,coalesce([ECO_In_Field].[InFieldIName],'') as InFieldIName
    
            ,coalesce([ECO_Uudet_Osat].[Item_Name],'') as Item_Name
            ,coalesce([ECO_Uudet_Osat].[Item_Description],'') as Item_Description
            ,coalesce([ECO_Uudet_Osat].[Item_New_rev],'') as Item_New_rev
            ,coalesce([ECO_Uudet_Osat].[Disp_Notes],'') as Disp_Notes
    
            ,coalesce([ECO_Uudet_Osat].[Reason_for_change],'') as Reason_for_change
    
            ,coalesce([ECO_Req_Change].ReqChangeName ,'') as [Requested_change]
            ,coalesce([ECO_Uudet_Osat].[Eco_name],'') as Eco_name
            ,coalesce([ECO_Item_Junction].[New_Price],'') as New_Price
            ,coalesce([ECO_Item_Junction].[Old_revision_qty],'') as Qty
    
            FROM [Laatu2].[dbo].[ECO_Uudet_Ecot] join ECO_Uudet_Osat on ECO_Uudet_Ecot.ECO_Name=ECO_Uudet_Osat.Eco_name 
            full join [Laatu2].[dbo].[Enumerot] on ECO_Uudet_Ecot.ECO_Originator = Enumerot.Enumero
            join ECO_In_Process as a on ECO_Uudet_Osat.In_Process = a.InProcessID
            join ECO_In_Process as b on ECO_Uudet_Osat.In_Order = b.InProcessID
            join ECO_In_Process as c on ECO_Uudet_Osat.In_Stock =c.InProcessID
            join ECO_In_Process as d on ECO_Uudet_Osat.Field_Return = d.InProcessID
            join ECO_In_Field on ECO_Uudet_Osat.In_Field = ECO_In_Field.InFieldID
            join ECO_Req_Change on ECO_Uudet_Osat.Requested_change = ECO_Req_Change.ReqChangeID
            left join ECO_Item_Junction on ECO_Uudet_Osat.Eco_name = ECO_Item_Junction.ECO_name and ECO_Uudet_Osat.Item_Name = ECO_Item_Junction.Item_Name
            
    
            order by [ECO_Uudet_Ecot].ECO_Name"""

        rows = self.cursor.execute(ddd).fetchall()
        for row in rows:

            muuttuja = row.Item_Name
            if muuttuja is None:
                muuttuja = ""
                lista10.append(muuttuja)
            else:
                lista10.append(muuttuja)

            muuttuja = row.Item_Description
            if muuttuja is None:
                muuttuja = ""
                lista11.append(muuttuja)
            else:
                lista11.append(muuttuja)

            muuttuja = row.Item_New_rev
            if muuttuja is None:
                muuttuja = ""
                lista12.append(muuttuja)
            else:
                lista12.append(muuttuja)

            muuttuja = row.New_Price
            if muuttuja is None:
                muuttuja = ""
                lista13.append(muuttuja)
            else:
                lista13.append(muuttuja)

            muuttuja = row.Qty
            if muuttuja is None:
                muuttuja = ""
                listaqty.append(muuttuja)
            else:
                listaqty.append(muuttuja)

            muuttuja = row.Prosessissa
            if muuttuja is None:
                muuttuja = ""
                lista14.append(muuttuja)
            else:
                lista14.append(muuttuja)

            muuttuja = row.Orderissa
            if muuttuja is None:
                muuttuja = ""
                lista15.append(muuttuja)
            else:
                lista15.append(muuttuja)

                muuttuja = row.Stockissa
            if muuttuja is None:
                muuttuja = ""
                lista16.append(muuttuja)
            else:
                lista16.append(muuttuja)

                muuttuja = row.Fieldilta
            if muuttuja is None:
                muuttuja = ""
                lista17.append(muuttuja)
            else:
                lista17.append(muuttuja)

            muuttuja = row.InFieldIName
            if muuttuja is None:
                muuttuja = ""
                lista18.append(muuttuja)
            else:
                lista18.append(muuttuja)

            muuttuja = row.Disp_Notes
            if muuttuja is None:
                muuttuja = ""
                lista19.append(muuttuja)
            else:
                lista19.append(muuttuja)

            muuttuja = row.Reason_for_change
            if muuttuja is None:
                muuttuja = ""
                lista20.append(muuttuja)
            else:
                lista20.append(muuttuja)

            muuttuja = row.Requested_change
            if muuttuja is None:
                muuttuja = ""
                lista21.append(muuttuja)
            else:
                lista21.append(muuttuja)

            muuttuja = row.Eco_name
            if muuttuja is None:
                muuttuja = ""
                lista22.append(muuttuja)
            else:
                lista22.append(muuttuja)

            muuttuja = row.ECO_Originator
            if muuttuja is None:
                muuttuja = "External User"
                originator_list.append(muuttuja)
            else:
                originator_list.append(muuttuja)

            muuttuja = row.Nimi
            if muuttuja is None:
                muuttuja = "External User"
                originator_list_name.append(muuttuja)
            else:
                originator_list_name.append(muuttuja)

        self.cnxn.commit()
        zip_table4 = zip(lista22, lista10, lista11, lista12, lista14, lista15, lista16, lista17, lista18, listaqty,
                         lista20,
                         lista21, originator_list, originator_list_name)
        eco_table4 = list(zip_table4)
        return eco_table4





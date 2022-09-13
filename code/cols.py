import utilities

#store csv data, get functions for each
class cols:
    #TODO
    #single dependent klass column - dont know what this is

    utilobj=utilities.utilities()

    #x data: independent unskipped columns
    x = utilobj.get_indep_data()
    x_dict = utilobj.convert_data_list_to_dict(x)

    #y data: dependent unskipped columns
    y = utilobj.get_dep_data()
    y_dict = utilobj.convert_data_list_to_dict(y)

    #all data
    all = utilobj.get_all_data()
    all_dict = utilobj.convert_data_list_to_dict(all)

    #all column names including skipped names 
    all_column_names = all[0]

    #all unskipped column names 
    all_unskipped_column_names = x[0]+y[0]

    #get functions start from here
    def get_x_data(self):
        return self.x
    
    def get_x_data_dict(self):
        return self.x_dict

    def get_y_data(self):
        return self.y

    def get_y_data_dict(self):
        return self.y_dict
    
    def get_all_data(self):
        return self.all
    
    def get_all_data_dict(self):
        return self.all_dict
    
    def get_all_col_names(self):
        return self.all_column_names
    
    def get_all_unskipped_col_names(self):
        return self.all_unskipped_column_names


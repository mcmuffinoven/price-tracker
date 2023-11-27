import React, {useState, useEffect, useMemo}  from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridValueGetterParams, GridRenderCellParams} from '@mui/x-data-grid';
import { WarningOutlined, CheckCircleOutline } from '@mui/icons-material';
import { Chip,ChipProps } from '@mui/material';
import { red, green } from '@mui/material/colors';
import Stack from '@mui/material/Stack';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import CircularProgress from '@mui/material/CircularProgress';

import cats from "./products.json"


export default function DataTable(props:any) {

  const [tableData, setTableData] = useState<any>([]);
  const [loading, setLoading] = useState(false);
  const CategoryType = {
    Tech: "Tech" ,
    Grocery: "Grocery" ,
    Fashion: "Fashion", 
    Cosmetics: "Cosmetics", 
    All: "All"
  };

  const [categoryType, setCategory] = useState("All");
  const colDef:GridColDef[] = []
  const arr:any[] = [];
  
  useEffect(() => {
    setLoading(true)
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        // Loading message on load
        setTableData(data)
        }).finally(()=>{
          setLoading(false)
        })
        }, []);

  if (!loading && tableData.length!=0){
    // Should probably hard code these cols 
          
    for (const [key, value] of Object.entries(tableData[0].productList[0])) {
      const parameters:any = {
        field:key,
        headerName: key,
        type: "string",
        width: 150,
        editable: false,
      }
      if (key == "saleBool"){
        parameters['renderCell'] = (params:any) => {
          return <Chip variant="outlined" sx={{justifyContent:"center"}} size="small" {...getChipProps(params)} />;
        }
      }
      if(key == "productLink"){
        parameters['renderCell'] = (params:any) => {
          return <a href={params.value} target="_blank">{params.value}</a>
        }
      }
      colDef.push(parameters)
    }

    function getChipProps(params: GridRenderCellParams): ChipProps {
      if (params.value === false) {
        return {
          icon: <WarningOutlined style={{ fill: red[500], }} />,
          style: {
            borderColor: red[500]
          },
          label:"No Sale",
          color:"error"
        };
      } else {
        return {
          icon: <CheckCircleOutline style={{ fill: green[500] }} />,
          style: {
            borderColor: green[500]
          },
          label:"Sale",
          color:"success"
        };
      }
    }
    
    // Should probably hard code these rows
    tableData.map((item:any)=>{ 
      item.productList.map((row:any)=>{
        if (row.category == categoryType){
          arr.push(row)
        }
        if (categoryType == "All"){
          arr.push(row)
        }
      })
    })
  }

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <Stack>
        <FormControl sx={{ width: '200px', pb: 1 }}>
          <InputLabel id="category-selector">Category</InputLabel>
          <Select
            labelId="category-selector"
            id="category-type"
            value={categoryType}
            label="Category"
            onChange={(event: SelectChangeEvent<string>) => {
              setCategory(event.target.value);
            }}
          >
            <MenuItem value={CategoryType.All}>All</MenuItem>
            <MenuItem value={CategoryType.Tech}>Tech</MenuItem>
            <MenuItem value={CategoryType.Grocery}>Grcoery</MenuItem>
            <MenuItem value={CategoryType.Fashion}>Fashion</MenuItem>
            <MenuItem value={CategoryType.Cosmetics}>Cosmetics</MenuItem>
          </Select>
        </FormControl>

        {loading ? (<CircularProgress />):(

        <DataGrid
          rows={arr}
          columns={colDef}
          initialState={{
            pagination: {
              paginationModel: {
                pageSize: 25,
              },
            },
          }}
          pageSizeOptions={[5]}
          checkboxSelection={false}
          disableRowSelectionOnClick
          columnVisibilityModel={{id:false}}
        />
        )}
      </Stack>
    </Box>
  );
}
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Typography from '@mui/material/Typography';
import Box from "@mui/material/Box"
import { AccessTime } from "@mui/icons-material";
import Rating from "@mui/material/Rating";

export interface Prod{
    id:number
    productName: string
    currentProductPrice: number
    lowestProductPrice: number
    lowestProductPriceDate: string
    trackedSinceDate: string
    category: string
}

export interface Category{
    category: string
    productList: Prod[]
}

export const TourCard = ({obj}:any) =>{
    return (
        <Grid item xs ={3}>
            <Paper elevation={3}>
                <img
                    src="https://tcproduction.blob.core.windows.net/media/%7B240f8b72-1159-4fd3-a150-0a837f50ba4a%7D.2573758641_297d6d19fa_o.jpg"
                    alt=""
                    className="img"/>
                <Box paddingX={1}>
                    <Typography component="h2" variant="subtitle1">
                        Niagra Falls
                    </Typography>
                    <Box
                        sx={{
                            display: "flex",
                            alignItems: "center",
                        }}
                        marginTop={3}
                    >
                        <AccessTime sx={{width:12.5}}/>
                        <Typography variant="body2" component="p" marginLeft={0.5}>{obj.currentProductPrice}</Typography>
                    </Box>
                    <Box 
                        sx={{
                            display: "flex",
                            alignItems: "center"
                        }}
                        > 
                        <Rating name="read-only" value={4.5} readOnly precision={0.5} size="small"/>
                            <Typography variant="body2" component="p" marginLeft={0.5}>Lowest:{obj.lowestProductPrice}</Typography>
                            <Typography variant="body3" component="p" marginLeft={1.5}>Tracked Since: {obj.trackedSinceDate}</Typography>
                    </Box>
                    <Box >
                        <Typography variant="h6" component="h3" marginTop={0}>{obj.productName}</Typography>
                    </Box>
                </Box>
            </Paper>
        </Grid>
    )
}
import React,{Component} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';

const styling = makeStyles({
    
    root: {
        minWidth: 100,
      },
      bullet: {
        display: 'flex',
        margin: '0 2px',
        transform: 'scale(0.8)',
      },
      title: {
        fontSize: 14,
      },
      pos: {
        marginBottom: 12,
      },
    });
    const styling2 = makeStyles((theme) => ({
      root: {
        display: 'flex',
        '& > *': {
          margin: theme.spacing(1),
          width: theme.spacing(16),
          height: theme.spacing(16),
        },
      },
    }));

class Result extends Component{
    render(){
        return(<div className={styling2.root}>
                <Paper variant="outlined" square elevation= {24}    />
                <Card className={styling.root} variant="outlined" raised="false" id="card"  >
            <CardContent>
            <Typography className={styling.title} color="textPrimary" align="center"  variant="h4" id="type"  >Description:</Typography>
            <Typography className={styling.title} color="textPrimary" align="left"  variant="h6" id="type"  >Run time </Typography>
               <Typography variant='body1' align='left'>ONNX Runtime is a cross-platform, high performance ML inferencing and training accelerator which is used.</Typography>
               <Typography className={styling.title} color="textPrimary" align="left"  variant="h6" id="type"  >Negative Score</Typography>
               <Typography variant='body1' align='left'> The Negative probability score of a person having Pneumonia.If the Negative score  is higher than the Positive sore then the person does not have Pneumonia.
               </Typography>
               <Typography className={styling.title} color="textPrimary" align="left"  variant="h6" id="type"  >Positive Score</Typography>
               <Typography variant='body1' align='left'> The positive probability score of a person having Pneumonia.If the Positive score is higher than the Negative sore then the person has Pneumonia.
               </Typography>
               </CardContent>
               </Card>
               
               </div>);
    }
    
}
export default Result;
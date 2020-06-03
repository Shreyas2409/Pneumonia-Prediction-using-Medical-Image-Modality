import React,{Component} from 'react';
import Box from '@material-ui/core/Box';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Yes from '../components/samples/about-me.jpg';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import { Divider } from '@material-ui/core';

// to display information about Pneumonia
const disp = makeStyles({
  root: {
    minWidth: 1,
  },
  bullet: {
    display: 'flex',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 20,
  },
  pos: {
    marginBottom: 24,
  },
});


class About extends Component{
    render()
    {
        return(<div>
         <Paper  variant="outlined" square elevation= {24} id='pa2'>
         <Grid container spacing={24}>
         <Grid item xs={6}>
         < img src={Yes}   />
         </Grid>
         </Grid>
         <Grid item xs={6} alignContent={'center'}>
          <Typography className={disp}  color='textPrimary'  variant='h4' align='center'> Pneumonia </Typography>
          <Typography className={disp}  color='textPrimary' >
          Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.

          Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.
          </Typography>
          </Grid>
          <Divider orientation='horizontal' />
          <Box alignContent={'center'}>
          <h4> Symptoms</h4>
          <ul>
          
    <li>Chest pain when you breathe or cough.</li>
    <li>Confusion or changes in mental awareness.</li>
   <li>Cough, which may produce phlegm.</li>
   <li> Fatigue.</li>
    <li>Fever, sweating and shaking chills.</li>
    <li>Lower than normal body temperature. </li>
   <li> Nausea, vomiting or diarrhea.</li>
    </ul>
            
          </Box>
         </Paper>
        </div>
              
        );
    }
}
export default About;

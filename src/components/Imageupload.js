import React from 'react';
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';

//this is used to style the card component which contains the form which takes image as an input
const useStyles = makeStyles({
    root: {
      minWidth: 1,
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
  const useStyles2 = makeStyles((theme) => ({
    root: {
      display: 'flex',
      '& > *': {
        margin: theme.spacing(1),
        width: theme.spacing(16),
        height: theme.spacing(16),
      },
    },
  }));
  



class ImageUpload extends React.Component {
    
    constructor(props) {
        super(props)
        this.state = {
            file : null,
            inferenceResult : null
        }
        
        this.onFormSubmit = this.onFormSubmit.bind(this)
        this.uploadImage = this.uploadImage.bind(this)

    }
    //function that executed when the form is submitted
    onFormSubmit(e) {
        console.log("Input, form")
        e.preventDefault()
        
        var formData = new FormData()
        formData.append("image", this.state.file)
        
        this.uploadImage(formData).then((data) => data.data).then((result) => {
            this.setState({inferenceResult : result}, () => console.log(this.state))
        }).catch((err) => alert(err))
    }
    //function sends the input to the api 
    uploadImage(imageFormData) {
        
        return axios.post("http://localhost:5000/api/infer", imageFormData, {
            "Content-Type" : "multipart/form-data"
        })
    }
    
    
    
    render() {
        console.log('hello')
        return (
            <div className={useStyles2.root} >
            <Paper variant="outlined" square elevation= {24}    />
            
            <Card className={useStyles.root} variant="outlined" raised="false" id="card" height={'100%'} >
            <CardContent>
            <Typography className={useStyles.title} color="textPrimary" align="center"  variant="h4" id="type"  >Upload a Chest X-ray image in jpeg format</Typography>
            <br></br>
            <form onSubmit = {this.onFormSubmit}> 
              <input type = "file"  accept="image/jpeg" onChange = {(e) => {
                  this.setState({file : e.target.files[0]}, () => {
                      console.log(this.state)
                  }) 
              }
            }/>

              <Button type = "submit" variant="outlined" color="primary" size="small" id="bu"> Upload </Button>
            </form>
            {
              //the output is returned 
              (this.state.inferenceResult) && (
                  <div style = {{margin : "20px auto", padding : "20px"}} >
                  <Typography className={useStyles.title} color="textPrimary" align="center"  variant="h4" id="type"  >Inferece Result</Typography>
               <Typography className={useStyles.title} color="textPrimary" align="center"  variant="h6" id="type">  <p>Runtime : {this.state.inferenceResult.runtime}</p></Typography>
               <Typography className={useStyles.title} color="textPrimary" align="center"  variant="h6" id="type">   <p>Negative  score : {(this.state.inferenceResult.result[0][0][0] * 100).toFixed(3)}</p></Typography>
                <Typography className={useStyles.title} color="textPrimary" align="center"  variant="h6" id="type"><p>Positive score : {(this.state.inferenceResult.result[0][0][1] * 100 ).toFixed(3)}</p> </Typography>
                  </div>
              )
            }
            </CardContent>
            </Card>
            </div>
        )
    }
}

export default ImageUpload;
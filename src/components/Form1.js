import React, {Component} from 'react';
//form example needs improvements
class Form1 extends Component{
 render(){
        return (
            <div class="form">
            <form action="http://localhost:5000/api/infer" method="post" encType="multipart/form-data" onSubmit={this.onForm}>
                     <input type="file" name="image"/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
   
}
export default Form1;



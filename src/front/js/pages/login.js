import React, {useState} from 'react';
import {useNavigate} from 'react-router-dom';

export const Login= () => {

    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const [error, setError] = useState()
    
    const handleLogin=(event) => {
    
        event.preventDefault()
        
        fetch()
    }

    return (

        <div>



        </div>

    )

}

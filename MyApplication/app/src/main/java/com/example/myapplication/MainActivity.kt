package com.example.myapplication

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.myapplication.ui.theme.MyApplicationTheme


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyApplicationTheme {
                Home()
            }
        }
    }
}

@Composable
fun Home() {
    Surface(modifier = Modifier.fillMaxSize(), color = Color(0xFFF6F6F6)) {
        Column(
            modifier = Modifier.padding(top = 50.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(25.dp),
        ) {
            Title()
            ButtonGoogle()
            ButtonSignIn()
            ButtonCreateAccount()
        }
    }
}


@Composable
fun Title() {
    Text(
        "Perch",
        color = Color.Blue,
        fontSize = 65.sp,
    )
}

@Composable
fun ButtonGoogle() {
    val context = LocalContext.current
    ExtendedFloatingActionButton(
        containerColor = Color.White,
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp),

        text = { Text("Continue with Google") },

        onClick = {
                  //implement google auth
        },
        icon = {
            Icon(
                painter = painterResource(id = R.drawable.google),
                "",
                tint = Color.Unspecified,
                modifier = Modifier.size(40.dp)
            )
        },
        elevation = FloatingActionButtonDefaults.elevation(8.dp),

    )
}

@Composable
fun ButtonSignIn() {
    ExtendedFloatingActionButton(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp),
        containerColor = Color.Blue,
        contentColor = Color(0xFFFFFFFF),
        text = { Text("Login with Email") },
        onClick = {

        },
        icon = {
            Icon(
                painter = painterResource(id = R.drawable.email),
                "",
                tint = Color.Unspecified,
                modifier = Modifier.size(25.dp)
            )
        },
        elevation = FloatingActionButtonDefaults.elevation(8.dp)
    )
}


@Composable
fun ButtonCreateAccount() {
    ExtendedFloatingActionButton(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp),
        content = {
            Text("Create an Account")
        },
        containerColor = Color.Blue,
        contentColor = Color(0xFFFFFFFF),
        onClick = {
            // integerate create account page
        }
    )
}


import { useUser } from '@auth0/nextjs-auth0/client';
import LoginView from './LoginView';
import { Login } from '@mui/icons-material';


export default function Index() {
  const { user, error, isLoading } = useUser();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>{error.message}</div>;

  if (user) {
    console.log(user)
    return (
      <div>
        Welcome {user.name}! <a href="/api/auth/logout">Logout</a>
        <LoginView user={user}></LoginView>
      </div>
    );
  }

  return <a href="/api/auth/login">Please Login</a>;
}
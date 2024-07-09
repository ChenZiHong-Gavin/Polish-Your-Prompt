import { Menu, Badge } from "react-daisyui"


const MenuTitle = () => {
    return (
        <Menu.Title  className="flex flex-row items-center">
            <img src="/logo.png" alt="logo" className="flex-none w-12 h-12" />
            <button href="#" className="flex-1 text-4xl font-bold text-blue-600 pl-4">Po-Prompt</button>
        </Menu.Title>
    );
}

const SideBar = ({ children }) => {
    return (
        <div>
            <Menu className="bg-base-200 w-80 h-screen rounded-box border-2 border-solid border-gray-250">
                <MenuTitle />
                <Menu.Item>
                    <button>Item 1</button>
                </Menu.Item>
                {/* <Menu>
                    <Menu.Item>
                        <a>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                            </svg>
                            Inbox
                            <Badge size="sm">99+</Badge>
                        </a>
                    </Menu.Item>
                    <Menu.Item>
                        <a>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            Updates
                            <Badge color="warning" size="sm">
                                NEW
                            </Badge>
                        </a>
                    </Menu.Item>
                    <Menu.Item>
                        <a>
                            Stats
                            <Badge color="info" size="xs" />
                        </a>
                    </Menu.Item>
                </Menu> */}
            </Menu>
        </div>
    );
}

export default SideBar;

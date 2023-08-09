/*
 * @lc app=leetcode.cn id=71 lang=cpp
 *
 * [71] 简化路径
 */

// @lc code=start
class Solution {
public:
    string simplifyPath(string path) {
        std::vector<std::string> names;
        std::stringstream ss(path);
        std::string name;

        while (getline(ss,name,'/')){
            names.push_back(name);
        }

        std::vector<std::string> stack;

        for( const auto& name: names){
            // 常指针 &代表name可以改变names内容 auto自动推断name类型
            std::cout<<name<<std::endl;

            // if(name=='..'){
            if(name==".."){
                if (!stack.empty()){
                    stack.pop_back();
                }
            }
            // else if (!name.empty() && name!='.'){
            // ''和""不一样
            else if (!name.empty() && name!="."){
                stack.push_back(name);
            }
        }

        std::stringstream result;
        result<<"/";
        for (size_t i=0;i<stack.size();++i){
            result<<stack[i];
            if(i!=stack.size()-1){
                result<<'/';
            }
        }
        return result.str();
    }
};

/*
class Solution {
public:
    string simplifyPath(string path) {

        // 分割字符串为列表形式
        std::vector<std::string> names;
        std::stringstream ss(path);
        std::string name;
        
        while (getline(ss, name, '/')) {
            names.push_back(name);
        }

        // 利用栈来处理
        std::vector<std::string> stack;

        // 访问列表里面的元素
        for (const auto& name : names) {
            std::cout << name << std::endl;
            // 1、如果是 ..
            if (name == "..") {
                // 在栈不为空的情况下
                if (!stack.empty()) {
                    // 弹出栈顶元素
                    stack.pop_back();
                }
            }
            // 2、如果是有效值
            // 字母
            else if (!name.empty() && name != ".") {
                stack.push_back(name);
            }
        }

        std::stringstream result;
        result << "/";
        for (size_t i = 0; i < stack.size(); ++i) {
            result << stack[i];
            if (i != stack.size() - 1) {
                result << "/";
            }
        }

        return result.str();

    }
};
*/
// @lc code=end


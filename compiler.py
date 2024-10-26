import os
import subprocess
import re

class Compiler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.plugin_name = "UnnamedPlugin"  # Default plugin name
        self.java_code = ""

    def parse(self):
        with open(self.source_file, 'r') as file:
            lines = file.readlines()

        # Extract plugin information
        self.extract_info(lines)

        # Parse the remaining code
        self.java_code += f"public class {self.plugin_name} extends JavaPlugin {{\n"
        self.java_code += "    @Override\n"
        self.java_code += "    public void onEnable() {\n"
        self.java_code += f"        getLogger().info(\"{self.plugin_name} Enabled\");\n"
        self.java_code += "        main();\n"
        self.java_code += "    }\n\n"

        # Parse function definitions and other constructs
        for line in lines:
            result = self.process_line(line.strip())
            if result:
                self.java_code += result + "\n"

        self.java_code += "}\n"  # Close the class

    def extract_info(self, lines):
        for line in lines:
            if line.startswith("#info"):
                continue
            elif line.startswith("name:"):
                self.plugin_name = line.split("name:")[1].strip().strip('"')
            # Further extraction for version, author, and Minecraft version can be added here

    def process_line(self, line):
        # Function for handling different line types
        if line.startswith("func"):
            return self.process_function(line)
        elif line.startswith("loop"):
            return self.process_loop(line)
        elif line.startswith("if"):
            return self.process_if(line)
        elif line.startswith("elif"):
            return self.process_elif(line)
        elif line.startswith("else"):
            return self.process_else(line)
        elif line.startswith("def"):
            return self.process_minecraft_function(line)
        elif re.match(r'^\w+\s*=\s*\[.*\]$', line):
            return self.process_data_structure(line)
        elif line.startswith("print("):
            return self.process_print(line)
        elif line.startswith("#") or line == "":
            return f"    // {line}"  # Comment handling
        return f"    {line}"  # Regular line

    def process_function(self, line):
        # Extract function name and parameters
        match = re.match(r'func\s+\[(.*?)\]\s*\((.*?)\):', line)
        if match:
            variables = match.group(1)
            name = match.group(2)
            return f"    public void {name}({variables}) {{\n        // Function logic here\n        return;\n    }}"
        return ""  # Return empty string if no match

    def process_loop(self, line):
        # Extract loop variable
        match = re.match(r'loop\((.*?)\):', line)
        if match:
            name = match.group(1)
            return f"    while (true) {{\n        // Looping logic here\n        // break;\n    }}"
        return ""  # Return empty string if no match

    def process_if(self, line):
        # Extract condition
        match = re.match(r'if\s+\[(.*?)\]\s*=\s*\[(.*?)\]:', line)
        if match:
            variable = match.group(1)
            value = match.group(2)
            return f"    if ({variable} == {value}) {{\n        // If logic here\n    }}"
        return ""  # Return empty string if no match

    def process_elif(self, line):
        # Extract condition
        match = re.match(r'elif\s+\[(.*?)\]:', line)
        if match:
            condition = match.group(1)
            return f"    else if ({condition}) {{\n        // Else if logic here\n    }}"
        return ""  # Return empty string if no match

    def process_else(self, line):
        return "    else {\n        // Else logic here\n    }"

    def process_minecraft_function(self, line):
        # Extract function name and parameter
        match = re.match(r'def\s+on_(\w+)\((.*?)\):', line)
        if match:
            event = match.group(1)
            param = match.group(2)
            return f"    public void on{event.capitalize()}({param}) {{\n        // Event handling logic here\n    }}"
        return ""  # Return empty string if no match

    def process_data_structure(self, line):
        # Handle list, dictionary, set, tuple
        if "list" in line:
            return f"    List<String> list = new ArrayList<>(); // List initialization"
        elif "dict" in line:
            return f"    Map<String, String> dict = new HashMap<>(); // Dictionary initialization"
        elif "set" in line:
            return f"    Set<String> set = new HashSet<>(); // Set initialization"
        elif "tuple" in line:
            return f"    Object[] tuple = new Object[3]; // Tuple initialization"
        return ""  # Return empty string if no match

    def process_print(self, line):
        # Extract the message to print
        match = re.match(r'print\((.*?)\)', line)
        if match:
            message = match.group(1)
            return f"    for (Player p : Bukkit.getOnlinePlayers()) {{\n        p.sendMessage({message});\n    }}"
        return ""  # Return empty string if no match

    def compile_to_jar(self):
        # Write the Java code to a file
        java_filename = f"{self.plugin_name}.java"
        with open(java_filename, 'w') as file:
            file.write(self.java_code)

        # Compile the Java file
        subprocess.run(["javac", java_filename])
        # Create the JAR file
        subprocess.run(["jar", "cvf", f"{self.plugin_name}.jar", f"{self.plugin_name}.class"])

    def run(self):
        self.parse()
        self.compile_to_jar()

if __name__ == "__main__":
    compiler = Compiler("main.void")
    compiler.run()

import org.bukkit.plugin.java.JavaPlugin;

public class {plugin_name} extends JavaPlugin {
    @Override
    public void onEnable() {
        getLogger().info("{plugin_name} Enabled");
        main();
    }

    public void main() {
        // Plugin main logic here
        System.out.println("Hello, Minecraft!");
    }
}

package club.dortware.modules;
@Module(name = "KillAura", bind = "G", category = "Combat")
public class KillAura
{
  
  @Subscriber
  void onTick(TickEvent event)
  {
    this.kill = true;
    mc.thePlayer = null;
  }
}
